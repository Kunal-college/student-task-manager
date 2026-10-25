
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'kunal123borse/student-task-manager'
    }

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
                bat '"C:\\Users\\KUNAL\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t %DOCKER_IMAGE%:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    bat '''
                        @echo off
                        echo %DOCKERHUB_TOKEN% | "C:\\Users\\KUNAL\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" login -u %DOCKERHUB_USER% --password-stdin
                        if errorlevel 1 exit /b 1
                        "C:\\Users\\KUNAL\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" push %DOCKER_IMAGE%:latest
                        if errorlevel 1 exit /b 1
                        "C:\\Users\\KUNAL\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'CI/CD image build and Docker Hub push completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
