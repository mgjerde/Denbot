pipeline{
    agent { dockerfile true }
    
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