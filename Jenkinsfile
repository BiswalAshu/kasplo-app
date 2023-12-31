// pipeline {
//     agent any

//     stages {
//         stage('Check Docker') {
//             steps {
//                 script {
//                     sh 'docker --version'
//                 }
//             }
//         }
//         // other stages
//     }
// }




pipeline {
    agent any

    environment {
        KUBECONFIG = credentials('kubeconfig')
        DOCKERHUB_CREDENTIALS = credentials('dhub')
        NAMESPACE = 'kasplo-app'
        IMAGE_NAME = 'biswalashu/kasplo-frontend'
        GIT_REPO_URL = 'https://github.com/BiswalAshu/kasplo-app.git'
        GITHUB_CREDENTIALS = credentials('github')
        GIT_BRANCH = 'frontend'
    }

    stages {

        stage('Checkout Source') {
            steps {
                git url: GIT_REPO_URL, branch: GIT_BRANCH
                // script {
                //     // Checkout code from GitHub
                //     checkout scm
                // }

            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                        def customImage = docker.build("${IMAGE_NAME}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}'
                    sh 'docker push ${IMAGE_NAME}:${BUILD_NUMBER}'
                }
            }
        }

        stage('Deploy App') {
            steps {
                script {
                    kubeconfig(credentialsId: 'kubeconfig', serverUrl: '') {
                        sh "kubectl set image deployment/nginx-deployment nginx=biswalashu/kasplo-frontend:${BUILD_NUMBER}"
                        sh "docker rmi -f biswalashu/kasplo-frontend:${BUILD_NUMBER}"
                    }
                }
            }
        }
    }
}
