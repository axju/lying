pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('setup') {
            steps {
                cleanWs()
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "pip install --user --upgrade pip setuptools wheel coverage nose"
                }
            }
        }
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "python setup.py sdist bdist_wheel"
                }
            }
        }
        stage('test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "nosetests --with-xunit --all-modules --traverse-namespace --with-coverage --cover-package=lying --cover-inclusive"
                    sh "python -m coverage xml --include=lying*"
                }
            }
            post {
                always {
                    junit 'nosetests.xml'
                    step([$class: 'CoberturaPublisher', autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', failUnhealthy: false, failUnstable: false, maxNumberOfBuilds: 0, onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false])
                }
            }
        }
    }
}
