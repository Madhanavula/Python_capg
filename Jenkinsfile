pipeline {
    agent any

    stages {
        stage('Clean ') {
            steps {
                cleanWs()   
            }
        }
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Madhanavula/Python_capg.git'
            }
        }

        stage('Verify') {
            steps {
                sh 'pwd'
                sh 'ls -lrt'
            }
        }
    }
}
