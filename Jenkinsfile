pipeline{

    environment {
        registry = "mgjerde/denbot"
        registryCredential = credentials('mgjerde-dockerhub')
    }
    
    agent any
    
    stages{
        stage('Building image') {
            steps{
                script{            
                    echo registryCredential
                    def customImage = docker.build(registry + ":${env.BUILD_ID}")
                    customImage.push()
                }
            }
        }
        stage('Deploy Image') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}