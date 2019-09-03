pipeline {
  agent { docker { image 'python:3.7.2' } }
  environment {
        projectName = 'ProjectTemplate'
        VIRTUAL_ENV = "${env.WORKSPACE}/venv"
    }
  stages {
    stage ('Install_Requirements') {
            steps {
                sh """
                    echo ${SHELL}
                    [ -d venv ] && rm -rf venv
                    #virtualenv --python=python2.7 venv
                    python -m venv venv
                    #. venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    pip install --upgrade pip
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
                    python -m unittest discover -v
                """
            }
        }

  }
}
