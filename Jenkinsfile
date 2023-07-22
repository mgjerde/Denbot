pipeline{
    agent {  
        label 'dock'
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