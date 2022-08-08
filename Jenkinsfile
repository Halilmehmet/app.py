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
                bat ("docker run ${env.BUILD_ID} --expose 8000 -v ./app:/app")
                
                }
            }
        
   
    }
}
