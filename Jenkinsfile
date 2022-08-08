pipeline {
    agent any
    
    stages {
        stage('Build') { 
            steps { 
                bat ("docker-compose build  -t ${env.BUILD_ID}   ." )
                bat ("docker-compose up  ${env.BUILD_ID}")
                }
            }
        
        
   
    }
}
