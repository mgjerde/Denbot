pipeline{

    environment {
        registry = "mgjerde/denbot"
        registryCredential = credentials('mgjerde-dockerhub')
    }
    
    agent any


    stages{
        def app
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
                        app.push()
                    }
                }
            }
        }
    }
}