from flask import Flask
from elasticsearch import Elasticsearch
from flask_apscheduler import APScheduler
import requests

es = Elasticsearch(hosts=[{"host": "host.docker.internal", "port": 9200}])
app = Flask(__name__)
sheduler = APScheduler()

URL = "https://halfiyatlaripublicdata.ibb.gov.tr/api/HalManager/getProductPricebyProductId"
TabelaGId= {
  "item": {
    "TabelaGId": "53a6756e-b99b-4039-8338-2e6a5c5db8c1"

  }
}
configurations = {
    "settings": {
        "index": {"number_of_replicas": 2},

    },
    "mappings": {
        "properties": {
            "id": {"type": "long"},
            "UrunAd": {"type": "text"},
            "EnDusukFiyat": {"type": "float"},
            "EnYuksekFiyat": {"type": "float"},
            "GuneAit": {"type": "date"}

        }
    }
}

def ibb():
    es.indices.create(index='ibb_hal', ignore=400, body=configurations)
    r = requests.post(url=URL, json=TabelaGId)
    j = r.json()

    for i in range(len(j['Results'])):
        EnDusukFiyat = j['Results'][i]['EnDusukFiyat']
        EnYuksekFiyat = j['Results'][i]['EnYuksekFiyat']
        UrunAd = j['Results'][i]['UrunAd']
        GuneAit = j['Results'][i]['GuneAit']
        data = {
            "id": i,
            "UrunAd": UrunAd,
            "EnDusukFiyat": EnDusukFiyat,
            "EnYuksekFiyat": EnYuksekFiyat,
            "GuneAit": GuneAit
        }

        es.index(index="ibb_hal", id=i, body=data)


@app.route("/")
def index():
    return "ok"

if __name__ =="__main__":
    sheduler.add_job(id='ibb',func=ibb ,trigger='interval',seconds= 900)
    sheduler.start()
    app.run(host='0.0.0.0', port=8000, debug=True)