pipeline {
  agent any 
    stages {
      stage("checking scm") {
        steps {
          checkout scm
          }
         }
       stage("build docker") {
        steps {
          sh "docker --version"
          }
         }
       stage("running docker") {
        steps {
          sh "whoami"
          }
        }
       stage("testing") {
        steps {
          sh "echo success"
          }
         }
     }
  }
  
