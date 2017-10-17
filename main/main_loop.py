import sys
import threading
import datetime
sys.path.insert(0, '../db')
import shelve
from CryptoCheck import check_Divergence, check_Spike
import requests as rqst
    
def main():
    def Cryptolog():
    	allCoins = 'BTC,ETH,XRP,BCH,LTC,DASH,XEM,NEO,XMR,MIOTA,ETC,LSK,ZEC,WAVES,STRAT,XLM,ARK,STEEM,EOS,GN'        # String containing the top 20 coins
    	request_string = rqst.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms='+allCoins)          # Request to the CryptoCompare API to obtain the exchange rates of the top 20 coins
    	coin_dict = request_string.json()                                                                           # Save the return of the Cryptocompare API request in a variable as a dictionary
    	return coin_dict
    
    coin_dict = Cryptolog()																	# Pass the dictionary to a variable outside the function

    userDB = shelve.open('../db/persondb')													# Open the user database
    
    #Go through the Divergence subscribes
    DivergenceDB = shelve.open('../db/personDivergenceDB')                                  # Open database for divergence service
    
    i = 1
    while i <= len(DivergenceDB['DivergenceServiceList'].members)-1:                        # Go through the list of divergence service instances to perform notification checks
    
        userID =  DivergenceDB['DivergenceServiceList'].members[i][0]                       # Retrieve the userID for each listed service instance
        userServicePosition = DivergenceDB['DivergenceServiceList'].members[i][1]           # Retrieve the position of the service instance in the list
    
        coin1 = DivergenceDB[userID].Services[userServicePosition - 1][0]                   # Retrieve coin1 for the service instance
        coin2 = DivergenceDB[userID].Services[userServicePosition - 1][1]                   # Retrieve coin2 for the service instance
        user_signal = float(DivergenceDB[userID].Services[userServicePosition - 1][2])      # Retrieve user_signal for the service instance

        for user in userDB:                                                                 # Retrieve user_name corresponding to the ID of this instance
            print(userDB[user])                                                             # A hash table will be implemented combining IDs with usernames
            if userDB[user].serviceID == userID:                                            #to avoid this search that takes time
                #print(user)
                user_name = user
                print("username is: "+str(user))
    
                first_name = userDB[user_name].first_name									# Retrieve first name corresponding to the ID of this instance
                telephone = userDB[user_name].telephone										# Retrieve telephone corresponding to the ID of this instance

        ex_rate = float(coin_dict[coin2])/float(coin_dict[coin1])                           # Calculate the exchange rate of interest fo this service instance
    
        i+=1
    
        check_Divergence(coin1, coin2, user_signal, ex_rate, first_name, telephone)         # Pass all the variable retrieved above to call the check function to determine if notification is necessary
    
    DivergenceDB.close()                                                                    # Close database for this Service
    
    #Go through the Spike subscribes
    
    SpikeDB = shelve.open('../db/personSpikeDB')                                            #Open database for Spike service
    
    i = 1
    while i <= len(SpikeDB['SpikeServiceList'].members)-1:                                  # Go through the list of divergence service instances to perform notification checks
    
        print("")
        userID =  SpikeDB['SpikeServiceList'].members[i][0]                                 # Retrieve the userID for each listed service instance
        print(userID)
        userServicePosition = SpikeDB['SpikeServiceList'].members[i][1]                     # Retrieve the position of the service instance in the list
    
        coin1 = SpikeDB[userID].Services[userServicePosition - 1][0]                        # Retrieve coin1 for the service instance
        user_signal = float(SpikeDB[userID].Services[userServicePosition - 1][2])           # Retrieve user_signal for the service instance
        direction = SpikeDB[userID].Services[userServicePosition - 1][3]                    # Retrieve user_signal for the service instance
    
        print(direction)
        print(user_signal)
    
        for user in userDB:                                                                 # Retrieve user_name corresponding to the ID of this service instance
    
            if userDB[user].serviceID == userID:
                print(userDB[user])
                user_name = user
    
                first_name = userDB[user_name].first_name
                telephone = userDB[user_name].telephone

                print(telephone)

        price = float(1/coin_dict[coin1])                                                    # Calculate the necessary exchange rate to perform check for this service instance
        print(price)
    
        i+=1
    
        check_Spike(coin1, user_signal, price, direction, first_name, telephone)             # Pass all the variable retrieved above to call the check function to determine if notification is necessary
    
    SpikeDB.close()
    
    
    userDB.close()                                                                           #Close userDB at the end of the whole check cycle
    
def Repeater():
    main()
    threading.Timer(15, Repeater).start()

Repeater()

###
### Add username - userID join table, saved in another shelve DB to avoid the for loop
###

### Add code to ensure that initializeDB runs on first time