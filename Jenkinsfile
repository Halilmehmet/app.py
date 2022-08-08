pipeline {
    agent any
    
    stages {
        stage('Build') { 
            steps { 
                bat ("docker-compose build " )
                bat ("docker-compose up  ${env.BUILD_ID}")
                }
            }
        stage('UP') { 
            steps { 
              bat ("docker-compose up  t ${env.BUILD_ID}")
               
                }
            }
        
   
    }
}
