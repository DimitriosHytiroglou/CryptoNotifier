
class Person:
    def __init__(self, name, job = None, pay = 0):  # Constructor takes three arguments
        self.name = name  # Fill out fields when created
        self.job = job  # self is the new instance object
        self.pay = pay

    def lastName(self):  # Behavior methods
        return self.name.split()[-1]  # self is implied subject

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))  # Must change here only

    def __repr__(self):  # Added method
        return '[Person: %s, %s]' % (self.name, self.pay)  # String to print

class Manager(Person):                          # Define a subclass of Person  which inherits Person attributes
    def __init__(self, name, pay):  # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)  # Run original with 'mgr'

    def giveRaise(self, percent, bonus=.10):  # Redefine to customize
        Person.giveRaise(self, percent + bonus)  # Good: augment original

class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')                         # Test the class
    sue = Person('Sue Jones', job='dev', pay=100000)  # Runs __init__ automatically
    print(bob)
    print(sue)
    print(bob.name, bob.pay)                          # Fetch attached attributes
    print(sue.name, sue.pay)                          # sue's and bob's attrs differ
    print(bob.lastName(), sue.lastName())  # Use the new methods
    sue.giveRaise(.10)  # instead of hardcoding
    print(sue.pay)
    print(sue)
    #tom = Manager('Tom Jones', 'mgr', 50000)  # Make a Manager: __init__
    tom = Manager('Tom Jones', 50000)  # Job name not needed:
    tom.giveRaise(.10)  # Runs custom version
    print(tom.lastName())  # Runs inherited method
    print(tom)
    print('--All three--')
    for obj in (bob, sue, tom):  # Process objects generically
        obj.giveRaise(.10)  # Run this object's giveRaise
        print(obj)  # Run the common __repr__

    development = Department(bob, sue)  # Embed objects in a composite
    development.addMember(tom)
    development.giveRaises(.10)  # Runs embedded objects' giveRaise
    development.showAll()  # Runs embedded objects' __repr__