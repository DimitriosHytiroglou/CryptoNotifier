#Write code that loops through the 2 Service lists and checks each user
# Then checks the exchange rates array
# And finally if needed calls twilio to send text
import sys
sys.path.insert(0, '../db')
import shelve


#Go through the Divergence subscribes
DivergenceDB = shelve.open('../db/personDivergenceDB')

for userService in DivergenceDB['DivergenceServiceList'].members:
    print(userService)


#Go through the Spike subscribes



#Add code to ensure that initializeDB runs on first time