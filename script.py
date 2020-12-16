import requests
import sys

user_id = ''
token = ''
branch_name = "newbranch"
source_branch = "master"
cl_data = sys.argv

for i in range(1, len(sys.argv)):
    if cl_data[i] == '-uid':
        user_id = cl_data[i + 1]
    elif cl_data[i] == '-token':
        token = cl_data[i + 1]
    elif cl_data[i] == '-name':
        branch_name = cl_data[i + 1]
    elif cl_data[i] == '-source':
        source_branch = cl_data[i + 1]

response = requests.get('https://www.gitlab.com/api/v4/users/' + user_id + '/projects', data={'PRIVATE-TOKEN': token})
print(response.status_code)

if response.status_code != 200:
    exit("Error while connecting to API \n Check UserID, AccessToken oe your Internet connection")

response = tuple(response.json())
i = 0
ids = []
d = {'key': 'value'}

for project in response:
    ids.append(project['id'])
    d[project['id']] = project['name']

if len(ids) > 0:
    print("Trying to make branches")
    for project_id in ids:
        if(requests.post('https://www.gitlab.com/api/v4/projects/' + str(project_id) + '/rpository/branches',
                         headers={'PRIVATE-TOKEN': token},
                         data={'branch': branch_name, 'ref': source_branch}).status_code) == 201:
            print("Created branch " + branch_name + " in project " + d[project_id])
        else:
            exit("Something went wrong. Check if branch already exist")
else:
    exit("No projects found!!!")
