pipeline {
  agent {
    kubernetes {}
  }
  stages {
    stage('st1') {
      steps {
        sh 'echo HOLA'
      }
    }

    stage('st2') {
      parallel {
        stage('st2') {
          steps {
            echo 'HECHO!'
          }
        }

        stage('noerror') {
          steps {
            sh 'exit 0'
          }
        }

        stage('st1a') {
          steps {
            sh 'sleep 30'
          }
        }
        stage('st1b') {
          steps {
            sh 'sleep 40'
          }
        }

        stage('st1c') {
          steps {
            sh 'sleep 20'
          }
        }
        stage('st1d') {
          steps {
            sh 'sleep 60'
          }
        }

        stage('noerror2') {
          steps {
            sh 'exit 0'
          }
        }

      }
    }

  }
}
