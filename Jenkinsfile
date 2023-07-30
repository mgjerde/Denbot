def app

pipeline{

    environment {
        registry = "mgjerde/denbot"
        registryCredential = 'mgjerde-dockerhub'
    }
    }
    
    agent any


    stages{
        stage('Building image') {
            steps{
                script{
                    app = docker.build(registry + ":${env.BUILD_ID}")
                }
            }
        }
        stage('Deploy Image') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                        app.push('latest')
                    }
                }
            }
        }
    }
}