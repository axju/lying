pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install .'
      }
    }
    stage('test') {
      steps {
        sh 'python -m unittest discover -v'
      }
    }
  }
}
