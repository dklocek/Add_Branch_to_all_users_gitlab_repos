Project stack:
- <i> GitLab API </i>
- <i> Python basics + requests </i>

Entrypoint: script.py

Script can add or remove branches from all repositories of specified user in Gitlab

Adding Branches

<code>script.py -s \<server URL> -id \<user ID> -t \<Access Token> -n \<new branch name> -sb \<source branch name> </code><br>
Parameters
<pre>
-server or -s        Server URL like http://gitlab.example.com   -default https://gitlab.com <br>
-id                  Gitlab user ID      - REQUIRED<br>
-token or -t         Access Token        - REQUIRED<br>
-name or -n          New branch name                             -default NewBranch<br>
-source or -sb       Source Branch for new created branch        -default master<br>
</pre>
Removing Branches<br>

<code>script.py -r -s \<server URL> -id \<user ID> -t \<Access Token> -n \<branch name><br> </code><br>
Parameters
<pre>
-remove or -r        Tell the script that you want to remove branches - REQUIRED to remove
-server or -s        Server URL like http://gitlab.example.com   -default https://gitlab.com<br>
-id                  Gitlab user ID      - REQUIRED<br>
-token or -t         Access Token        - REQUIRED<br>
-name or -n          Branch name                                  -default NewBranch<br></pre>

