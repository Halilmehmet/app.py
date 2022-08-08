pipeline {
    agent any
    
    stages {
        stage('Build') { 
            steps { 
                sh '''
                  docker-compose build
                '''
                }
            }
        }
        stage('up'){
            steps {
                sh '''
                  docker-compose up -t $(env.BUILD_ID)
                '''
                }
        }
        
    }
}