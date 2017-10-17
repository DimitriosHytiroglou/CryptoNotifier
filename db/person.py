
class User():
    def __init__(self, first_name, last_name, telephone, user_name):        # Constructor takes four arguments
        self.first_name = first_name                                        # Fill out fields when created
        self.last_name = last_name                                          # self is the new instance object
        self.telephone = telephone                                          # ...
        self.user_name = user_name                                          # ...

        import random                                                       # Create a unique ID for the user
        self.serviceID = str(random.getrandbits(128))                       # Thsi is used to identify him across the databases

    def __repr__(self):  # Added method
        return '[User: %s, %s, %s]' % (self.first_name, self.last_name, self.telephone)  # String to print in command line or log

    def updateFirstName(self, new_first_name):                    ### These functions are not currently used,
        print("Old name: ", self.first_name)                      ### but could be in a future implementation to better efficiency
        self.first_name = new_first_name                          ### ...
        print("--- changed to ---")                               ### ...
        print("New name: ", self.first_name)                      ### ...

    def updateLastName(self):                                     ### ...
        print(self.Last_Name)                                     ### ...

# Service Classes #

class Service():                                        # Superclass defining a Service 
    def __init__(self, *args):                          # Services have members subscribed to them
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def showAll(self):                                  # Show all members of a service, this would be used by the system administrator
        for person in self.members:
            print(person)

class DivergenceService(Service):                       # Class describing the Divergence services 
    def __init__(self, *args):
        Service.__init__(self, *args)
        self.members = list(args)

class SpikeService(Service):                            # Class describing the Spike services
    def __init__(self, *args):
        Service.__init__(self, *args)
        self.members = list(args)


# Service Member classes #

class MemberServices():                                             # Class describinng the services subscribed to by a certain user
    def __init__(self, currency1, currency2, price):                # Initiates the list of Services for the user
        self.Services = []                                          # This is used by the initializedb.py
        self.Services.append([currency1, currency2, price])

    def addService(self, currency1, currency2, price):
        self.Services.append([currency1, currency2, price])


class MemberDivergenceServices(MemberServices):                     # Class describinng the Divergence services subscribed to by a certain user       
    def __init__(self, currency1, currency2, price):
        MemberServices.__init__(self, currency1, currency2, price)

    def addService(self, currency1, currency2, price):
        self.Services.append([currency1, currency2, price])

class MemberSpikeServices(MemberServices):                          # Class describinng the SPike services subscribed to by a certain user
    def __init__(self, currency1, currency2, price, direction):
        MemberServices.__init__(self, currency1, currency2, price)
        self.Services[len(self.Services)-1].append(direction)

    def addService(self, currency1, currency2, price, direction):
        self.Services.append([currency1, currency2, price, direction])


def initializeServices():                                           # Initializes an instance of each Service class with an empty list
    return DivergenceService("init"), SpikeService("init")          # Used by initializedb.py


if __name__ == '__main__':
    pass
