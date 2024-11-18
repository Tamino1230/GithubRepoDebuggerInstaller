# main code
by = "tamino1230" 
main = "" # "" by default | your main file of the project. You need to fill that out.
notdelete = ["mainDebugger.py", "config.py", "click and extract me.bat"] # files which are not gonna get deleted at a reinstall.
branch = "main" # main by default. | the github branch everything is getting downloaded

# repo settings
repoOwner = "github_repo_owner" # github_repo_owner by default. The owner of the repo your downloading from.
repoName = "example_reposition" # reposition name
# private repo?
repo = True # True by default | True = private repo, False = public repo
# dont want to put in your token everytime?
TokenFastUse = False # True = Yes, False = No
fastToken = "example_token" # If you want to use fastToken please DO NOT share you file.
# if you use it for a private repo. The Token it needs the right permissions to do that: https://www.github.com/settings/tokens
# Permissions needed: 
# repoFull, repo, repo_deploymentAccess, public_repoAccess, repo:inviteAccess, security_eventsRead, write security events
# write:packages, read:packages 

# time
waiter = 0.1 # 0.1 by default.

# tasks register
# task getting recorded?
doTasks = True # True = yes, False = no | True by default
taskFailed = 0 # 0 by default.
taskSuccess = 0 # 0 by default.
operationNumber = 1 # 1 by default.

# missing data list config
missList = [] # nothing by default

# all actual files getting you have in your project you want to download registered
# paths in github

file1 = "file1.html" # delete this file after
file2 = "file2.py" # delete this file after
file3 = "file3.js" # delete this file after
file4 = "folder/file4" # delete this file after
file5 = "folder/folder2/file5" # delete this file after

# you can add new sites here: please use unique names:

# all files you have put above you have to put them in here:
allfiles = [file1, file2, file3, file4, file5] # delete file1-5