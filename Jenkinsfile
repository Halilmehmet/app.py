pipeline {
    agent any
    
    stages {
        stage('Build') { 
            steps { 
                bat ("docker build  -t ${env.BUILD_ID}  ." )
                }
            }
        stage('UP') { 
            steps { 
                bat ("docker run ${env.BUILD_ID} -p 8000:8000 -v ./app:/app")
                
                }
            }
        
   
    }
}
