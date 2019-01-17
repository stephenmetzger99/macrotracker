import sys
import copy
import twitterscraper2 as ts

def listAllUsers():
    for user in userList:
        print(user)

#broken because .txt file stores \n at the end of each line which doesn't allow equality verification
def removeUser(userList):
    print("type user's handle with no '@' sign (ex: 'elonmusk')\n")
    usrIn = input("Enter account to remove: ")
    userIn = usrIn + "\n"
    for user in userList[:]:
        if (usrIn == user):
            print("hi")
            userList.remove(usrIn)
    
    
def addUser():
    print("type user's handle with no '@' sign (ex: 'elonmusk')\n")
    newUser = input("Enter a new user to follow: ")
    userList.append(newUser)
    i = 0
    with open("twitterusers.txt", "w") as user_file:
        for user in userList:
            user_file.write(user)  
        print("Updated User List")
        
    user_file.close()
    
def menu():
    print("\nEdit list of twitter accounts: \n\t1. List Users\n\t2. Add User\n\t3. Remove user\n\t4. Update feed\n\t0. Exit")
    usrIn = input("Choice: ")
    userInput = int(usrIn)
    
    if (userInput == 1):
        listAllUsers()
    elif (userInput == 2):
        addUser()
    elif (userInput == 3):
        removeUser(userList)
    elif (userInput == 4):
        ts.feedUpdater()
    elif (userInput == 0):
        sys.exit()
    else:
        menu()

    menu()
  
    
    
userList = []
with open ("twitterusers.txt") as twitter_username_file:
    for line in twitter_username_file:
        userList.append(line)
menu()

        
        


        


