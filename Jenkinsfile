pipeline {
    agent any
    
    stages {
        stage('Build') { 
            steps { 
                bat ("docker-compose build " )
                
                }
            }
        stage('UP') { 
            steps { 
              bat ("docker-compose up  -t ${env.BUILD_ID} .")
               
                }
            }
        
   
    }
}
