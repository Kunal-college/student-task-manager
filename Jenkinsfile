
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'kunal123borse/student-task-manager'
        PYTHON = 'C:\\Users\\KUNAL\\AppData\\Local\\Python\\bin\\python.exe'
        DOCKER = 'C:\\Users\\KUNAL\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
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
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%PYTHON%" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER%" build -t %DOCKER_IMAGE%:latest .'
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
                        "%DOCKER%" logout
                        echo %DOCKERHUB_TOKEN% | "%DOCKER%" login --username %DOCKERHUB_USER% --password-stdin
                        if errorlevel 1 exit /b 1
                        "%DOCKER%" push %DOCKER_IMAGE%:latest
                        if errorlevel 1 exit /b 1
                        "%DOCKER%" logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
