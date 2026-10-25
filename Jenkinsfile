
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Kunal-college/student-task-manager.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\KUNAL\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\KUNAL\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\KUNAL\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" version'
bat '"C:\\Users\\KUNAL\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t student-task-manager:latest .'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
