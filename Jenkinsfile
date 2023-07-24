pipeline{
    agent { dockerfile true }
    
    stages{
        stage('Building image') {
            steps{
                def customImage = docker.build("mgjerde/denbot:${env.BUILD_ID}")
                customImage.push()
            }
        }   
    }
}