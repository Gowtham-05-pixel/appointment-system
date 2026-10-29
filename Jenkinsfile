
pipeline {
    agent any

    stages {
        stage('Checkout and Verify Files') {
            steps {
                echo 'Appointment System CI Pipeline Started'

                checkout scm

                echo 'Checking project files...'

                bat 'git --version'
                bat 'if exist v1\\app.py (echo Version 1 found) else (exit 1)'
                bat 'if exist v2\\app.py (echo Version 2 found) else (exit 1)'
                bat 'if exist v3\\app.py (echo Version 3 found) else (exit 1)'
                bat 'if exist docker\\Dockerfile (echo Dockerfile found) else (exit 1)'

                echo 'All project files verified successfully!'
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Docker images for all versions...'

                bat 'docker build -f docker/Dockerfile --build-arg APP_VERSION=v1 -t appointment-system:v1 .'
                bat 'docker build -f docker/Dockerfile --build-arg APP_VERSION=v2 -t appointment-system:v2 .'
                bat 'docker build -f docker/Dockerfile --build-arg APP_VERSION=v3 -t appointment-system:v3 .'

                echo 'All three Docker images built successfully!'
                bat 'docker images appointment-system'
            }
        }
    }
}
