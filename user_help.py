def user_help():
    print("Welcome, I'm happy that You are using this script. there is some help: \n\n"
          "You can add or remove branches from all your repositories at Gitlab \n\n"
          "Syntax: \n\n"
          "Adding Branches \n\n"
          "script.py -s <server URL> -id <user ID> -t <Access Token -n <new branch name> -sb <source branch name> \n\n"
          "-server or -s        Server URL like http://gitlab.example.com   -default https://gitlab.com\n"
          "-id                  Gitlab user ID      - REQUIRED\n"
          "-token or -t         Access Token        - REQUIRED\n"
          "-name or -n          New branch name                             -default NewBranch\n"
          "-source or -sb       Source Branch for new created branch        -default master\n\n"
          "Removing Branches \n\n"
          "script.py -r -s <server URL> -id <user ID> -t <Access Token -n <branch name>\n\n"
          "-server or -s        Server URL like http://gitlab.example.com   -default https://gitlab.com\n"
          "-id                  Gitlab user ID      - REQUIRED\n"
          "-token or -t         Access Token        - REQUIRED\n"
          "-name or -n          Branch name                                  -default NewBranch\n")
    exit(0)
