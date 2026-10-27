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
                    powershell '''
                        $ErrorActionPreference = "Stop"
                        $docker = $env:DOCKER

                        $env:DOCKERHUB_TOKEN |
                            & $docker login --username $env:DOCKERHUB_USER --password-stdin

                        if ($LASTEXITCODE -ne 0) {
                            throw "Docker Hub login failed"
                        }

                        & $docker push "${env:DOCKER_IMAGE}:latest"

                        if ($LASTEXITCODE -ne 0) {
                            throw "Docker Hub push failed"
                        }
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