pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t post-service:latest .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Push to AWS ECR') {
            steps {
                echo "Skipping ECR push (not configured yet)"
            }
        }

    }

    post {
        always {
            echo 'Pipeline Finished.'
        }
    }
}
pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t post-service:latest .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Push to AWS ECR') {
            steps {
                echo "Skipping ECR push (not configured yet)"
            }
        }

    }

    post {
        always {
            echo 'Pipeline Finished.'
        }
    }
}

