pipeline {
  agent any
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

        stage('error') {
          steps {
            sh 'exit 1'
          }
        }

      }
    }

  }
}