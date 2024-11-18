import os
import os.path
import time
import requests
import shutil  # reverse delete files
import config # config.py data

main = config.main
taskFailed = config.taskFailed
taskSuccess = config.taskSuccess
operationNumber = config.operationNumber
missList = config.missList
allfiles = config.allfiles
notdelete = config.notdelete
repo = config.repo
doTasks = config.doTasks
TokenFastUse = config.TokenFastUse
repo = config.repo
repoName = config.repoName
repoOwner = config.repoOwner
fastToken = config.fastToken
branch = config.branch

def dofastUse():
    global securecode
    global fastToken

    if TokenFastUse == True:
        securecode = fastToken
        print("Using fastToken.")
    elif TokenFastUse == False:
        print("Not using fastToken.")
        secure()
    else: 
        print(f"Undefined Variable: {TokenFastUse} has a wrong argument.")

def ifChecker():
    print("check if you want to check")

    if doTasks == True:
        print("Tasks are getting recorded.")
        checker()
    elif doTasks == False:
        print("Tasks are not getting recorded.")
    else:
        print(f"Variable: {doTasks} isnt True or False. Error accured")
        exit()

def checkConfig():
    print("Checking Config.py...")

    if os.path.exists("config.py") == True:
        print("Exists... \nContinue.")
    elif os.path.exists("config.py") == False:
        print("config.py doesnt exist. File cannot be loaded...")
        time.sleep(2)
        exit()
    else:
        print("Error accured. Download the latest version.")

def secure():
    if repo == True:
        global securecode
        print("Private Repo...")
        print("\nPlease Insert your personal Token from GitHub for using the Programm")
        securecode = input("Safe Insert here: ")
        print("-")

        # token
        GITHUB_TOKEN = securecode

        # get user informations
        url = 'https://api.github.com/user'

        # auth again
        headers = {
            'Authorization': f'token {GITHUB_TOKEN}'
        }

        # request the github api
        response = requests.get(url, headers=headers)

        # test of the connection
        if response.status_code == 200:
            print("Connection Worked! Passwort worked!.")
            user_info = response.json()
            print(f"Logged in User: {user_info.get('login')} \n Welcome!...")
        else:
            print(f"Connection Failed! Statuscode: {response.status_code}")
            if response.status_code == 401:
                print("Wrong passwort or no authorization.")
                exit()
    elif repo == False:
        print("Public Repo...")
    else:
        print(f"'Variable Repo' is: {repo}, not 'True' or 'False'...")
        exit()

def countdown():
    time.sleep(config.waiter*5)
    print("\n... ", end="")
    time.sleep(config.waiter*5)
    print("... ", end="")
    time.sleep(config.waiter*5)
    print("...\n")
    time.sleep(config.waiter*5)

def checkingFiles(filename, end):
    global taskSuccess
    global taskFailed
    global operationNumber
    global needRepair
    global file

    if end == True:
        file = filename
        if os.path.exists(file) == True:
            print(f"{file} exists")
            taskSuccess += 1
        else: 
            print(f"{file} doesn't exist")
            taskFailed += 1
            needRepair = True
            addMissingList()
        print(f"Operation {operationNumber} worked\n")
        time.sleep(config.waiter)
        
    if end == False:
        file = filename
        if os.path.exists(file) == True:
            print(f"{file} exists!")
            taskSuccess += 1
        else: 
            print(f"{file} doesn't exist!")
            taskFailed += 1
            needRepair = True
            addMissingList()
        print(f"Operation {operationNumber} worked\n")

        operationNumber += 1
        time.sleep(config.waiter)

def start():
    print("Checking if all needed Files exist...\n")
    countdown()

def totalInfo():
    print(f"\nTotal operations: {operationNumber}\nFailed Tasks: {taskFailed}\nSuccessful Tasks: {taskSuccess}")

def checker():
    if operationNumber == taskSuccess == True:
        print("All needed files exist\n")
    elif operationNumber != taskSuccess == False:
        print("Not all needed files exist\n")
    else: 
        print("Unknown Issue, please fix it\n")

def addMissingList():
    global missList
    missList.append(file)
    print("Adding to missing Files!")

def failedFix():
    try:
        if needRepair == True:
            wantRepair = input("Do you want your Files to be downloaded or repaired: (yes/no/reinstall): ")
            if wantRepair == "yes":
                print(f"answer {wantRepair}!\nPlease wait! Files are getting downloaded")
                time.sleep(config.waiter*2)
                countdown()
                downloadMissing()
                exit()
            elif wantRepair.lower() in ["no", "cancel"]:
                time.sleep(config.waiter)
                countdown()
                print(f"answer {wantRepair}!\nDownload canceled!")
                exit()
            elif wantRepair.lower() == "reinstall":
                time.sleep(config.waiter)
                print(f"answer {wantRepair}!\nPlease wait, everything is reinstalling!")
                time.sleep(config.waiter*2)
                countdown()
                reinstall()
                exit()
            else: 
                print(f"answer '{wantRepair}' is not available. Cancel download")
    except NameError as ignore: 
        print("Nothing needs to be fixed or downloaded.")

def reinstall():
    print("Reinstalling...\n")
    global allfiles
    global securecode

    GITHUB_TOKEN = securecode
    OWNER = repoOwner
    REPO = repoName
    BRANCH = branch
    allfiles = allfiles

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    def clean_directory():
        global notdelete
        for filename in os.listdir("."):
            if filename not in notdelete:
                file_path = os.path.join(".", filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"Deleted directory: {file_path}")

    def download_file_from_github(file_path):
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{file_path}?ref={BRANCH}"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            file_info = response.json()
            print("file_info:", file_info)

            if isinstance(file_info, dict) and 'download_url' in file_info:
                download_url = file_info['download_url']
                file_content = requests.get(download_url, headers=headers).content

                print("file_path:", file_path)
                dir_path = os.path.dirname(file_path)
                if dir_path:
                    os.makedirs(dir_path, exist_ok=True)

                with open(file_path, "wb") as file:
                    file.write(file_content)
                print(f"Successfully downloaded: {file_path}")
                return True
            elif isinstance(file_info, list):
                print("Warning: Received a list instead of a file. Check the file path.")
                return False
            else:
                print("Unexpected response format:", file_info)
                return False
        else:
            print(f"Error occurred while downloading: {file_path}: {response.status_code}")
            print("Answer from GitHub:", response.json())
            return False

    def download_all_files():
        clean_directory()
        for current_file in allfiles:
            success = download_file_from_github(current_file)
            if not success:
                print(f"Error while downloading: {current_file}. Try later.")
                break

    download_all_files()

def downloadMissing():
    global missList
    print(missList)
    print("Downloading Missing...\n")
    global securecode

    GITHUB_TOKEN = securecode
    OWNER = repoOwner
    REPO = repoName
    BRANCH = branch
    missList = missList

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    def download_file_from_github(file_path):
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{file_path}?ref={BRANCH}"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            file_info = response.json()
            print("file_info:", file_info)

            if isinstance(file_info, dict) and 'download_url' in file_info:
                download_url = file_info['download_url']
                file_content = requests.get(download_url, headers=headers).content

                print("file_path:", file_path)
                dir_path = os.path.dirname(file_path)
                if dir_path:
                    os.makedirs(dir_path, exist_ok=True)

                with open(file_path, "wb") as file:
                    file.write(file_content)
                print(f"Successfully downloaded: {file_path}")
                return True
            elif isinstance(file_info, list):
                print("Warning: Received a list instead of a file. Check the file path.")
                return False
            else:
                print("Unexpected response format:", file_info)
                return False
        else:
            print(f"Error occurred while downloading: {file_path}: {response.status_code}")
            print("Answer from GitHub:", response.json())
            return False

    while missList:
        current_file = missList[0]
        success = download_file_from_github(current_file)
        
        if success:
            missList.pop(0)
            print(f"Remaining Files: {missList}")
        else:
            print(f"Error while downloading: {current_file}. Try later.")
            break

def end():
    nowWhat = input("What do you want to do now? (reinstall/cancel)")
    if nowWhat.lower() == "reinstall":
        print("Please wait, everything is reinstalling!")
        time.sleep(config.waiter*2)
        print("Reinstalling...")
        countdown()
        reinstall()
    elif nowWhat.lower() == "cancel":
        print("\ncanceling...")
        countdown()
        print("canceled")
        exit()
    else: 
        print(f"answer {nowWhat} does not exist!")
        countdown()
        print("cancel...")
        exit()

# broadcast message.
checkConfig()
dofastUse()
start()
# files:
# example: checkingFiles(config.examplefile, True/False (True = Last File; False = every file except last))
checkingFiles(config.file1, False) # delete this file after.
checkingFiles(config.file2, False) # delete this file after.
checkingFiles(config.file3, False) # delete this file after.
checkingFiles(config.file4, False) # delete this file after.
# The last File needs to have the argument "True" at the end
checkingFiles(config.file5, True) # delete this file after.
# information feedback if wanted.
totalInfo()
# checks if everything is okay.
ifChecker()
failedFix()
# ending
end()
# print(missList) # test to check if its added to the missing list.

#   todo:
#   1. upload new files directly to github and make a new branch with a new name you can choose
#   2. (maybe) making a user interface (propably not)
#   3. a better errorcodehandling
#   4. making the program saver (database needed) (like everyone has a own code to use this program in case it got leaked)
#   

input('\nPress ENTER to quit ...')