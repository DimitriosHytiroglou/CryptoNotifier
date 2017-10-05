from person import User                                 # Load our classes

import shelve

def retrieveUser():
    key = input("Please provide your username: ")
    db = shelve.open('../db/persondb')                  # Open shelve database
    if key not in db:                                   # Check if username in database
        print("There is no such user name... sorry.")   #...
    else:
        #for key in sorted(db):                         # IGNORE THIS LINE
        print(key, '\t=>', db[key])                     # Print user details for that username
    db.close()                                          # Close after making changes


def addUser():
    first_name = input("Give first name: ")                        #Retrieve new user data
    last_name = input("Give last name: ")                          #...
    telephone = input("Give telephone: ")                          #...
    user_name = input("Give username: ")                           #...

    new_user = User(first_name, last_name, telephone, user_name)   #Create instance of class User with new data

    db = shelve.open('../db/persondb')                             # Open shelve database
    db[new_user.user_name] = new_user                              # Store new user object on shelve by key = username
    db.close()                                                     # Close shelve database after making changes


def updateUser():
    pass
#    db = shelve.open('../db/persondb')              # Reopen shelve with same filename
#
#    for key in sorted(db):                          # Iterate to display database objects
#        print(key, '\t=>', db[key])                 # Prints with custom format
#
#    #sue = db['Sue']                                # Index by key to fetch
#    #sue.updateFirstName("Josey")                   # Update in memory using class's method
#    #db['Sue'] = sue                                # Assign to key to update in shelve
#    #print(db['Sue'])
#    db.close()                                      # Close after making changes

def deleteUser():
    key = input("Give the username you want to delete: ")
    sure = input("Are you sure you want to delete this user? (Y/N)")
    if sure.lower() == "y":
        db = shelve.open('../db/persondb')
        del db[key]
        db.close()
        print("User deleted.")
    else:
        return
