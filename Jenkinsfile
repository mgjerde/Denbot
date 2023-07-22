pipeline{
    agent { dockerfile true }
    
    stages{
        stage('Building image') {
            steps{
                script {
                app = docker.build("mgjerde/denbot")
                }
            }
        }   
    }
}