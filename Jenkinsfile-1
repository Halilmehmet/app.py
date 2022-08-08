pipeline {
    agent any
    
    stages {
        stage('Build') { 
            steps { 
                bat (" " )
                
                }
            }
        stage('UP') { 
            steps { 
              bat ("docker-compose up  -t ${env.BUILD_ID} ")
               
                }
            }
        
   
    }
}
