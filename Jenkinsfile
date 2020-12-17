pipeline {
    agent any

    parameters {
        string(name: 'name', defaultValue: 'NewBranch', description: 'Name of new branch')
        string(name: 'source', defaultValue: 'master', description: 'Source for new branch')

    }

    stages {
        stage('Hello') {
            environment {
                GITLAB_TOKEN = credentials('GITLAB_TOKEN')
                GL_UID = credentials('GITLAB_UID')
            }
            steps {
                sh 'python3 script.py -id $GL_UID -n ${name} -sb ${source}'
            }
        }
    }
}
