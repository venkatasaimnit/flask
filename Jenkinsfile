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
          sh "docker build -t flaskapp ."
          }
         }
       stage("running docker") {
        steps {
          sh "docker run -dit -p 5001:5001 --name flask flaskapp"
          }
        }
       stage("testing") {
        steps {
          sh "echo success"
          }
         }
     }
  }
  
