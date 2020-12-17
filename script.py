from user_help import *
from actions import *
import sys
import os
server = "https://gitlab.com"
user_id = ''
token = os.getenv('GITLAB_TOKEN')
branch_name = "NewBranch"
source_branch = "master"
cl_data = sys.argv
add = True

for i in range(1, len(sys.argv)):
    if cl_data[i] == '-id':
        user_id = cl_data[i + 1]
    elif cl_data[i] == '-token' or cl_data[i] == '-t':
        token = cl_data[i + 1]
    elif cl_data[i] == '-name' or cl_data[i] == '-n':
        branch_name = cl_data[i + 1]
    elif cl_data[i] == '-source' or cl_data[i] == '-sb':
        source_branch = cl_data[i + 1]
    elif cl_data[i] == '-server' or cl_data[i] == '-s':
        server = cl_data[i + 1]
    elif cl_data[i] == '-help' or cl_data[i] == '-h':
        user_help()
    elif cl_data[i] == '-remove' or cl_data[i] == '-r':
        add = False

if user_id == '':
    exit("Provide GitLab User ID\n type -help or -h for help")
if token == '' or token is None:
    exit("Provide Access Token \n type -help or -h for help")
if branch_name == "NewBranch":
    print('Using "NewBranch" as name for creating branches')
if source_branch == "master" and add:
    print('Using "master" as a source for creating branches')
if server == "https://gitlab.com":
    print('Using "https://gitlab.com" as GitLab server for creating branches')

response = connect(server, user_id, token)
projects = get_projects(response)
if add:
    add_branches(server, token, branch_name, source_branch, projects)
else:
    remove_branches(server, token, branch_name, projects)
