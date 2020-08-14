pipeline {
  agent any
  stages {
    stage('st1') {
      steps {
        timestamps()
        sh 'echo HOLA'
      }
    }

    stage('st2') {
      steps {
        echo 'HECHO!'
      }
    }

  }
}