from person import User                         # Load our classes
from person import DivergenceService, SpikeService, MemberDivergenceServices, MemberSpikeServices

import shelve                                   #import shelve database module

def checkPassword():
    pass
    #import geatpass
    #check = False
    #while not check:
    #pass = getpass.getpass()
    #if pass == username.password:
    #    x = True
    #else:
    #    print("Wrong password!"


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
    key = input("Please provide your username: ")
    db = shelve.open('../db/persondb')  # Open shelve database

    if key not in db:  # Check if username in database
        print("There is no such user name... sorry.")  # ...

    else:
        print(key, '\t=>', db[key])  # Print user details for that username

    while True:
        print("\nSelect a the field you would like to update by typing the corresponding number:\n")       #Display menu text and instructions
        print("""1. Update username\n2. Update first name\n3. Update last name\n4. Update telephone""")
        user_in = input("\n> ")

        if user_in == "1":
            new_key = input("Please provide the new username: ")
            sure = input("Are you sure you want to update this username? (Y/N)")
            if sure.lower() == "y":
                db[new_key] = db[key]  # Store new user object on shelve by key = username
                del db[key]
                print("Username updated.")
        elif user_in == "2":
            pass
        elif user_in == "3":
            pass
        elif user_in == "4":
            pass
        else:
            break


    db.close()
#
# Choose between names, username, phone, and also add services
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


def addService():
    user_name = input("Give username: ")

    print("\nSelect what service you want to add by typing the corresponding number:\n")  # Display menu text and instructions
    print("""1. Divergence Notification Service\n2. Spike Notification Service""")
    user_in = input("\n> ")

    if user_in == "1":
        print("Divergence Notification Service selected.\nPlease provide your service requirements below:")
        currency1 = input("Choose the first currency: ")
        currency2 = input("Choose the second currency: ")
        divergence = input("Inpu the divergence in prices that you seek to me notified about: ")

        db = shelve.open('../db/persondb')

        ID = db[user_name].serviceID


        db[ID] = MemberDivergenceServices(currency1, currency2, divergence)


        db.close()


    elif user_in == "2":
        pass

    else:
        print("goob")

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
