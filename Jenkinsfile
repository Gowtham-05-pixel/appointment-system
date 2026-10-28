
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Appointment System CI Pipeline Started'
                checkout scm
            }
        }

        stage('Verify Project Files') {
            steps {
                echo 'Checking Appointment System project files...'
                bat 'git --version'
                bat 'dir'
                bat 'if exist v1\\app.py (echo Version 1 found) else (exit 1)'
                bat 'if exist v2\\app.py (echo Version 2 found) else (exit 1)'
                bat 'if exist v3\\app.py (echo Version 3 found) else (exit 1)'
                echo 'All three versions verified successfully!'
            }
        }
    }
}
