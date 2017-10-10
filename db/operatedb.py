from person import User                         # Load our classes
from person import DivergenceService, SpikeService, MemberDivergenceServices, MemberSpikeServices

import shelve                                   #import shelve database module

def checkPassword():
    pass
    #import getpass
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

    user_serviceID = db[key].serviceID
    db.close()                                          # Close after making changes

    print("\nThis user's services include: ")              # Call the retrieveUserServices function to print the services of this user
    retrieveUserServices(user_serviceID)


def retrieveUserServices(user_serviceID):
    #db = shelve.open('../db/persondb')  # Open shelve database
    DivergenceDB = shelve.open('../db/personDivergenceDB')          # Open the Divergence Services database

    if user_serviceID in DivergenceDB:                              #Check if there is an entry for this user in the database
        print("\nDivergence services: ")
        for services in DivergenceDB[user_serviceID].Services:      #Iterate through the Services of the user and print them
            print(services)

    DivergenceDB.close()

    SpikeDB = shelve.open('../db/personSpikeDB')                    # Open the Divergence Services database

    if user_serviceID in SpikeDB:                                   #Check if there is an entry for this user in the database
        print("\nSpike services: ")
        for services in SpikeDB[user_serviceID].Services:           #Iterate through the Services of the user and print them
            print(services)

    SpikeDB.close()

    #print(type(db[user_serviceID]))
    #else:
        #pass

    #db.close()


def addUser():
    first_name = input("Give first name: ")                        #Input new user data
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
        divergence = input("Input the divergence in prices that you seek to me notified about: ")

        db = shelve.open('../db/persondb')

        ID = db[user_name].serviceID

        DivergenceDB = shelve.open('../db/personDivergenceDB')

        if ID in DivergenceDB:
            tmp = DivergenceDB[ID]
            tmp.Services.append([currency1, currency2, divergence])
            DivergenceDB[ID] = tmp
        else:
            DivergenceDB[ID] = MemberDivergenceServices(currency1, currency2, divergence)  # Create a key in the database with the user's serviceID and a value of his specs

        position = len(DivergenceDB[ID].Services)
        List_tmp = DivergenceDB['DivergenceServiceList']        #Enter the added services to the list of active Diergence services
        List_tmp.members.append([ID,position])                  #...
        DivergenceDB['DivergenceServiceList'] = List_tmp        #...

        DivergenceDB.close()
        db.close()


    elif user_in == "2":
        print("Spike Notification Service selected.\nPlease provide your service requirements below:")
        currency1 = input("Choose the first currency: ")
        currency2 = input("Choose the second currency: ")
        divergence = input("Input the price that you seek to me notified about: ")
        relativity = input("Input whether you care about that price and higher or lower.(H/L)")

        db = shelve.open('../db/persondb')

        ID = db[user_name].serviceID

        SpikeDB = shelve.open('../db/personSpikeDB')

        if ID in SpikeDB:
            tmp = SpikeDB[ID]
            tmp.Services.append([currency1, currency2, divergence])
            SpikeDB[ID] = tmp
        else:
            SpikeDB[ID] = MemberSpikeServices(currency1, currency2, divergence, relativity)  # Create a key in the database with the user's serviceID and a value of his specs

        position = len(SpikeDB[ID].Services)
        List_tmp = SpikeDB['SpikeServiceList']  # Enter the added services to the list of active Diergence services
        List_tmp.members.append([ID, position])  # ...
        SpikeDB['SpikeServiceList'] = List_tmp  # ...

        SpikeDB.close()
        db.close()


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
