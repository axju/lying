pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('setup') {
      steps {
        bash 'python -m venv venv'
        bash 'source ./venv/bin/activate'
      }
    }
    stage('build') {
      steps {
        bash 'pip install .'
      }
    }
    stage('test') {
      steps {
        bash 'python -m unittest discover -v'
      }
    }
  }
}
