from person import User               # Load our classes

import shelve

def addUser():
    first_name = input("Give first name: ")                        #Retrieve new user data
    last_name = input("Give last name: ")                          #...
    telephone = input("Give telephone: ")                          #...
    user_name = input("Give username: ")                           #...

    new_user = User(first_name, last_name, telephone, user_name)   #Create instance of class User with new data

    db = shelve.open('../db/persondb')                             # Open shelve database
    db[new_user.user_name] = new_user                              # Store new user object on shelve by key = username
    db.close()                                                     # Close shelve database after making changes

