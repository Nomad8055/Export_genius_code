
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\EG-QA\\AppData\\Local\\Python\\bin\\python.exe'
    }

    stages {

        stage('Checkout Production Code') {
            steps {
                echo 'Production code checked out from GitHub'
            }
        }

        stage('Python Version') {
            steps {
                bat '''
                    if not exist "%PYTHON%" (
                        echo Python executable not found!
                        exit /b 1
                    )

                    "%PYTHON%" --version
                '''
            }
        }

        stage('Checkout QA Automation') {
            steps {
                dir('Qa_Testing_code') {
                    git branch: 'main',
                        url: 'https://github.com/Nomad8055/Qa_Testing_code.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('Qa_Testing_code') {
                    bat '''
                        "%PYTHON%" -m pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Install Playwright') {
            steps {
                dir('Qa_Testing_code') {
                    bat '''
                        "%PYTHON%" -m playwright install chromium
                    '''
                }
            }
        }

        stage('Run Automation Tests') {
            steps {
                dir('Qa_Testing_code') {
                    bat '''
                        "%PYTHON%" -m pytest tests -v --tb=short --junitxml=pytest-results.xml
                    '''
                }
            }
        }
    }

    post {
        always {
            junit(
                allowEmptyResults: true,
                testResults: 'Qa_Testing_code/pytest-results.xml'
            )
        }

        success {
            echo 'QA AUTOMATION PASSED'
        }

        failure {
            echo 'QA AUTOMATION FAILED'
        }
    }
}
