pipeline{
    agent { dockerfile true }
    
    stages{
        stage('Building image') {
            steps{
                def customImage = docker.build("my-image:${env.BUILD_ID}")
                customImage.push()
            }
        }   
    }
}