pipeline {
    agent any
    
    stages {
        stage('Build') { 
            steps { 
                bat ("docker build  -t ${env.BUILD_ID}   ." )
                bat ("docker run -p 8000:8000  ${env.BUILD_ID}")
                }
            }
        stage('UP') { 
            steps { 
                
                
                }
            }
        
   
    }
}
