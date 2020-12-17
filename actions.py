import requests


def connect(server, user_id, token):
    try:
        response = requests.get(server + '/api/v4/users/' + user_id + '/projects', data={'PRIVATE-TOKEN': token})
        print(str(response.status_code) + " - Connection established")

        if response.status_code != 200:
            exit("Error while connecting to API \n Check UserID and AccessToken")

        return response

    except Exception as e:
        exit('Connection failed please check \n'
             ' - if the server url is correct (http://<your server address)')


def get_projects(response):
    try:
        response = tuple(response.json())
    except Exception as e:
        exit("Response from host is not as expected \n"
             " Check if server url i correct \n"
             " for more info use script.py -help")

    projects = dict()

    for project in response:
        projects[project['id']] = project['name']
    del response
    return projects


def add_branches(server, token, branch_name, source_branch, projects_list):
    if len(projects_list) > 0:
        print("Trying to make branches")
        for project in projects_list:
            response = requests.post(server + '/api/v4/projects/' + str(project) + '/repository/branches',
                                     headers={'PRIVATE-TOKEN': token},
                                     data={'branch': branch_name, 'ref': source_branch})
            if response.status_code == 201:
                print("Created branch " + branch_name + " in project " + projects_list[project])
            elif response.status_code == 200:
                exit("Got response 200 instead of 201 \n"
                     "Check your server url (if www.gitlab.com be sure to use https:// instead of http://)")
            elif response.status_code == 400:
                print(branch_name + " probably exist already in project " + projects_list[project])
            elif response.status_code == 401:
                exit("401 - Authorization error, check if your token has needed access rights")
            else:
                exit("Something went wrong. Code:" + str(response.status_code))
    else:
        exit("No projects found!!!")


def remove_branches(server, token, branch_name, projects_list):
    if len(projects_list) > 0:
        print("Trying to remove branches")
        for project in projects_list:
            response = requests.delete(
                server + '/api/v4/projects/' + str(project) + '/repository/branches/' + branch_name,
                headers={'PRIVATE-TOKEN': token})
            if response.status_code == 204:
                print("Deleted branch " + branch_name + " in project " + projects_list[project])
            elif response.status_code == 200:
                exit("Got response 200 instead of 204 \n"
                     "Check your server url (if www.gitlab.com be sure to use https:// instead of http://)")
            elif response.status_code == 401:
                exit("401 - Authorization error, check if your token has needed access rights")
            elif response.status_code == 404:
                print("Branch " + branch_name + " didn't exist in project " + projects_list[project])
            else:
                exit("Something went wrong. Code:" + str(response.status_code))
    else:
        exit("No projects found!!!")

