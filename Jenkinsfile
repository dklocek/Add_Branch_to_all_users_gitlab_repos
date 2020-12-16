pipeline {
    agent any

    parameters {
        string(name: 'name', defaultValue: 'NewBranch', description: 'Name of new branch')
        string(name: 'source', defaultValue: 'master', description: 'Source for new branch')

    }

    stages {
        stage('Hello') {
            environment {
                GL_TOKEN = credentials('GITLAB_TOKEN')
                GL_UID = credentials('GITLAB_UID')
            }
            steps {
                git url: 'https://github.com/dklocek/Add_Branch_to_all_users_gitlab_repos.git'
                sh "python3 script.py -uid $GL_UID -token $GL_TOKEN -name $name -source $source"
            }
        }
    }
}