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
        IMAGE_NAME = 'biswalashu/kasplo-backend'
        GIT_REPO_URL = 'https://github.com/samir282/Dummy_FullStack_Project.git'
        GITHUB_CREDENTIALS = credentials('github')
        GIT_BRANCH = 'backend'
    }

    stages {

        stage('Checkout Source') {
            steps {
                git url: GIT_REPO_URL, branch: GIT_BRANCH
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
                        sh "kubectl set image deployment/backend-deployment backend=biswalashu/kasplo-backend:${BUILD_NUMBER} --record"
                    }
                }
            }
        }
    }
}
