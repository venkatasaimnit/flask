pipeline {
  agent any 
    stages {
      stage("Fix the permission issue") {

            agent any

            steps {
                sh "sudo chown root:jenkins /run/docker.sock"
            }

        }
      stage("checking scm") {
        steps {
          checkout scm
          }
         }
       stage("build docker") {
        steps {
          sh "sudo docker build -t flaskapp ."
          }
         }
       stage("running docker") {
        steps {
          sh "sudo docker run -dit -p 5001:5001 --name flask flaskapp"
          }
        }
       stage("testing") {
        steps {
          sh "echo success"
          }
         }
     }
  }
  
