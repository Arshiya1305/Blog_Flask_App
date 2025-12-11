pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', 'url: https://github.com/Arshiya1305/Blog_Flask_App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t post-service:ci ./microservices/post-service'
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests yet. Placeholder stage.'
            }
        }

        stage('Push to AWS ECR') {
            steps {
                echo 'Will configure in Step 3'
            }
        }
    }

    post {
        always {
            echo 'Pipeline Finished.'
        }
    }
}
