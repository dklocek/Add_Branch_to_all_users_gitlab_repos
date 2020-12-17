pipeline {
    agent any

    parameters {
        string(name: 'name', defaultValue: 'NewBranch', description: 'Name of new branch')
        string(name: 'source', defaultValue: 'master', description: 'Source for new branch')
        string(name: 'server', defaultValue: 'https://gitlab.com', description: 'GitLab Server URL')
        booleanParam(name: 'add', defaultValue: true, description: 'True - ADD, False - REMOVE')

    }
// when{ expression { params.action == 'apply'}}
    stages {
        stage('ADD BRANCH') {
            when{ expression { params.add }}
                environment {
                    GITLAB_TOKEN = credentials('GITLAB_TOKEN')
                    GL_UID = credentials('GITLAB_UID')
                }
                steps {
                    sh 'python3 script.py -s ${server} -id $GL_UID -n ${name} -sb ${source}'
                }
        }

        stage('REMOVE BRANCH') {
            when{ expression { !params.add }}
                environment {
                    GITLAB_TOKEN = credentials('GITLAB_TOKEN')
                    GL_UID = credentials('GITLAB_UID')
                    }
                    steps {
                        sh 'python3 script.py -remove -s ${server} -id $GL_UID -n ${name}'
                    }
                }
    }
}
