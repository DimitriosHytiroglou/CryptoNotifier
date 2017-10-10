import sys
sys.path.insert(0, '../db')

from person import User

def retrieve_user():
    from operatedb import retrieveUser
    retrieveUser()
    input("\nPress ENTER to continue\n")

def create_user():
    from operatedb import addUser
    addUser()
    input("\nPress ENTER to continue\n")

def update_user():
    from operatedb import updateUser
    updateUser()
    input("\nPress ENTER to continue\n")

def add_service():
    from operatedb import addService
    addService()
    input("\nPress ENTER to continue\n")

def delete_user():
    from operatedb import deleteUser
    deleteUser()
    input("\nPress ENTER to continue\n")


def main():

    user_in = ""       #Placeholder value for user input

    while True:
        print("Select a task by typing the corresponding number:\n")       #Display menu text and instructions
        print("""1. Retrieve user\n2. Create new user\n3. Update user\n4. Delete user\n5. Add service""")
        user_in = input("\n> ")

        if user_in.lower() == "exit":
            print("\nGood bye!")
            break

        if user_in == "1":
            retrieve_user()

        if user_in == "2":
            create_user()

        if user_in == "3":
            update_user()

        if user_in == "4":
            delete_user()

        if user_in == "5":
            add_service()

        #ADD Admin overide
            #print("Entered admin override mode!")
            #Show all users
            #Export all users in CSV

if __name__ == "__main__":
    main()