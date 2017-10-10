#Write code that loops through the 2 Service lists and checks each user
# Then checks the exchange rates array
# And finally if needed calls twilio to send text
import sys
sys.path.insert(0, '../db')
import shelve
from CryptoCheck import check_Divergence, check_Spike
import requests as rqst

#from CryptoAPI import CryptoFunction

#Exchange_rates = CryptoFunction                    #Get Library containing Crypto exchange rates


def Cryptolog():
    request_string = rqst.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=USD,BTC,BCH,ETH,LTC,LSK,NEO,XRP')
    coin_dict = request_string.json()
    return coin_dict

coin_dict = Cryptolog()
#Test Ether in Bitcoins 0.0615 0.061
#ex_rate = 1                                         #DELETE THIS EXAMPLE

userDB = shelve.open('../db/persondb')

#Go through the Divergence subscribes
DivergenceDB = shelve.open('../db/personDivergenceDB')

i = 1
while i <= len(DivergenceDB['DivergenceServiceList'].members)-1:

    userID =  DivergenceDB['DivergenceServiceList'].members[i][0]
    userServicePosition = DivergenceDB['DivergenceServiceList'].members[i][1]

    # print(userID)
    #print(userServicePosition)
    #print(DivergenceDB[userID].Services[userServicePosition - 1])

    coin1 = DivergenceDB[userID].Services[userServicePosition - 1][0]
    coin2 = DivergenceDB[userID].Services[userServicePosition - 1][1]
    user_signal = float(DivergenceDB[userID].Services[userServicePosition - 1][2])

    #print(coin1)
    #print(coin2)
    #print(user_signal)

    for user in userDB:
        print(userDB[user])
        if userDB[user].serviceID == userID:
            #print(user)
            user_name = user
            #print("username is: "+str(user))

            first_name = userDB[user_name].first_name
            telephone = userDB[user_name].telephone

            #print(first_name)
            #print(telephone)
    
    #print(coin_dict[coin1])
    #print(coin_dict[coin2])
    ex_rate = float(coin_dict[coin1])/float(coin_dict[coin2])

    i+=1

    check_Divergence(coin1, coin2, user_signal, ex_rate, first_name, telephone)

#Go through the Spike subscribes


####
#### Add username - userID join table, saved in another shelveto avoid the for loop
####

#Add code to ensure that initializeDB runs on first time