pipeline {
    agent any
    
    stages {
        stage('Build') { 
            steps { 
                bat '''
                 docker-compose build 
                '''
                }
            }
        stage('UP') { 
            steps { 
                bat '''
                 docker-compose up -d  -t ${'''env.BUILD_ID'''}
                '''
                }
            }
        
   
    }
}