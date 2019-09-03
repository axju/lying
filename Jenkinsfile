pipeline {
  agent { docker { image 'python:3.7.2' } }
  environment {
        projectName = 'ProjectTemplate'
        VIRTUAL_ENV = "${env.WORKSPACE}/venv"
    }
  stages {
    stage ('setup') {
            steps {
                sh """
                    echo ${SHELL}
                    [ -d venv ] && rm -rf venv
                    python -m venv venv
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    python -m pip install --upgrade pip wheel setuptools twine tox flake8 pylint pylama
                """
            }
        }

    stage ('build') {
            steps {
                sh """
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    pip install . e
                """
            }
        }

    stage ('test') {
            steps {
                sh """
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    tox
                """
            }
        }

  }
}
