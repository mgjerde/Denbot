pipeline{
    agent any
    
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