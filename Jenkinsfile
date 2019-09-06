pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "pip install --user --upgrade pip setuptools wheel"
                    sh "pip install --user ."
                }
            }
        }
        stage('test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "python -m unittest discover -v"
                }
            }
            post {
                cleanup {
                    cleanWs()
                }
            }
        }
    }
}
