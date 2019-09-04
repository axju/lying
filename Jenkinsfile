pipeline {
  agent none
  environment {
        projectName = 'ProjectTemplate'
        VIRTUAL_ENV = "${env.WORKSPACE}/venv"
    }
  stages {
    stage ('python:3.7') {
      agent { docker { image 'python:3.7' } }
        steps {
          sh """
            echo ${SHELL}
            [ -d venv ] && rm -rf venv
            python -m venv venv
            export PATH=${VIRTUAL_ENV}/bin:${PATH}
            python -m pip install --upgrade pip wheel setuptools
            pip install . e
            python -m unittest discover -v
        """
        }
    }
    stage ('python:3.8') {
      agent { docker { image 'python:3.7' } }
        steps {
          sh """
            echo ${SHELL}
            [ -d venv ] && rm -rf venv
            python -m venv venv
            export PATH=${VIRTUAL_ENV}/bin:${PATH}
            python -m pip install --upgrade pip wheel setuptools
            pip install . e
            python -m unittest discover -v
        """
        }
    }

  }
}
