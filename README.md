Project stack:
- <i> GitLab API </i>
- <i> Python basics + requests </i>

Entrypoint: script.py

Script can add or remove branches from all repositories of specified user in Gitlab

Adding Branches

<code>script.py -s <server URL> -id <user ID> -t <Access Token -n <new branch name> -sb <source branch name> </code>

-server or -s        Server URL like http://gitlab.example.com   -default https://gitlab.com <br>
-id                  Gitlab user ID      - REQUIRED
-token or -t         Access Token        - REQUIRED
-name or -n          New branch name                             -default NewBranch
-source or -sb       Source Branch for new created branch        -default master
Removing Branches
script.py -r -s <server URL> -id <user ID> -t <Access Token -n <branch name>
-server or -s        Server URL like http://gitlab.example.com   -default https://gitlab.com
-id                  Gitlab user ID      - REQUIRED
-token or -t         Access Token        - REQUIRED
-name or -n          Branch name                                  -default NewBranch

