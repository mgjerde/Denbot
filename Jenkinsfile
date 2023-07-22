pipeline{
    agent {  
        node {
            label 'docker' 
        }
        
    }
    
    stages{
        stage('Building image') {
            steps{
                script {
                def app = docker.build("mgjerde/denbot")
                }
            }
        }   
    }
}