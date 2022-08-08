pipeline {
    agent any
    
    stages {
        stage('Build') { 
            steps { 
                bat ("docker-compose build -d  -t ${env.BUILD_ID}")
                }
            }
        stage('UP') { 
            steps { 
                bat ("docker-compose up -d")
                
                }
            }
        
   
    }
}
