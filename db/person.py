
class User():
    def __init__(self, first_name, last_name, telephone, user_name):  # Constructor takes three arguments
        self.first_name = first_name  # Fill out fields when created
        self.last_name = last_name  # self is the new instance object
        self.telephone = telephone
        self.user_name = user_name

        import random
        self.serviceID = str(random.getrandbits(128))

    def __repr__(self):  # Added method
        return '[User: %s, %s, %s]' % (self.first_name, self.last_name, self.telephone)  # String to print

    def updateFirstName(self, new_first_name):
        print("Old name: ", self.first_name)  ##Placeholder text
        self.first_name = new_first_name
        print("--- changed to ---")
        print("New name: ", self.first_name)

    def updateLastName(self):
        print(self.Last_Name)


class Service():
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def showAll(self):
        for person in self.members:
            print(person)

class DivergenceService(Service):    ###This is the exchange divergence functionality
    def __init__(self, *args):
        Service.__init__(self, *args)
        self.members = list(args)

class SpikeService(Service):         ###This is the price spike functionality
    def __init__(self, *args):
        Service.__init__(self, *args)
        self.members = list(args)


### ServiceMember classes ###


class MemberServices():
    def __init__(self, currency1, currency2, price):
        self.Services = []          ###Initiates the list of Services for the user
        self.Services.append([currency1, currency2, price])

    def addService(self, currency1, currency2, price):
        self.Services.append([currency1, currency2, price])


class MemberDivergenceServices(MemberServices):
    def __init__(self, currency1, currency2, price):
        MemberServices.__init__(self, currency1, currency2, price)


class MemberSpikeServices(MemberServices):
    def __init__(self, currency1, currency2, price, direction):
        MemberServices.__init__(self, currency1, currency2, price)
        self.Services[len(self.Services)-1].append(direction)

    def addService(self, currency1, currency2, price, direction):
        self.Services.append([currency1, currency2, price, direction])


def initializeServices():                                       #Initializes an instance of each class with an empty list
    return DivergenceService("init"), SpikeService("init")


if __name__ == '__main__':
    pass

#    for obj in (bob, sue, tom):  # Process objects generically
#        obj.giveRaise(.10)  # Run this object's giveRaise
#        print(obj)  # Run the common __repr__
#
#    development = Department(bob, sue)  # Embed objects in a composite
#    development.addMember(tom)
#    development.giveRaises(.10)  # Runs embedded objects' giveRaise
#    development.showAll()  # Runs embedded objects' __repr__