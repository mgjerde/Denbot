pipeline{

    environment {
        registry = "mgjerde/denbot"
        registryCredential = credentials('mgjerde-dockerhub')
    }
    
    agent any

    def customImage 

    stages{
        stage('Building image') {
            steps{
                script{            
                    customImage = docker.build(registry + ":${env.BUILD_ID}")
                }
            }
        }
        stage('Deploy Image') {
            steps{
                script {
                    customImage.withRegistry( '', registryCredential ) {
                        customImage.push()
                    }
                }
            }
        }
    }
}