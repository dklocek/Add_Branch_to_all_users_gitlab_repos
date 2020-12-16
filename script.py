import requests
import sys
user_id = ''
token = ''
branch_name = "newbranch"
source_branch = "master"
cl_data = sys.argv

for i in range(1, len(sys.argv)):
    if cl_data[i] == '-uid':
        user_id = cl_data[i+1]
    elif cl_data[i] == '-token':
        token = cl_data[i+1]
    elif cl_data[i] == '-name':
        branch_name = cl_data[i+1]
    elif cl_data[i] == '-source':
        source_branch = cl_data[i+1]

r = requests.get('https://www.gitlab.com/api/v4/users/' + user_id + '/projects', data={'PRIVATE-TOKEN': token})
print(r.status_code)
if r.status_code != 200:
    exit("Error while connecting to API \n Check UserID, AccessToken oe your Internet connection")
jr = tuple(r.json())
i = 0
ids = []
for pr in jr:
    ids.append(pr['id'])

print("Trying to make branches")
for project_id in ids:
    print(
        requests.post('https://www.gitlab.com/api/v4/projects/' + str(project_id) + '/repository/branches',
                      headers={'PRIVATE-TOKEN': token},
                      data={'branch': branch_name, 'ref': source_branch}).status_code)
