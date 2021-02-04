pipeline {
    agent { docker { image 'python:3.8' } }
    stages {
        stage('setup') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "pip install --user --upgrade pip"
                    sh "pip install --user ."
                }
            }
        }
        stage('pytest') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "pip install --user --upgrade coverage pytest"
                    sh "python -m coverage run --branch --source lying -m pytest --junitxml junittest-coverage.xml"
                    sh "python -m coverage xml"
                }
            }
        }
        stage('pylint') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "python -m pip install pylint pylint_junit"
                    sh "python -m pylint --rcfile=setup.cfg --output-format=pylint_junit.JUnitReporter lying | tee junittest-pylint.xml"
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
    }
    post {
        always {
            junit allowEmptyResults: true, healthScaleFactor: 0.0, testResults: 'junittest*.xml'
            step([$class: 'CoberturaPublisher', autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', failUnhealthy: false, failUnstable: false, maxNumberOfBuilds: 0, onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false])
        }
        cleanup {
            cleanWs()
        }
    }
}
