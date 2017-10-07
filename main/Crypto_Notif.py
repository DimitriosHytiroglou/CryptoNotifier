import requests as rqst
import threading
import datetime

user1_list = [['BTC','ETH', 1.27], [ 'ETH', 'USD', 300.41]]


def request_maker():

	base = "https://min-api.cryptocompare.com/data/price?fsym="
	base_currency = []
	target_currencies = []

	for i in range(len(user1_list)):
		base_currency[i] = user1_list[i][0]

	pass
	#for i in range(len())


# def Cryptolog():
# 	request = rqst.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BCH,USD,EUR')

# 	log = open("Logs/Cryptolog.txt","a")

# 	log.write(str(datetime.datetime.now().time())+' - '+request.text+'\n')

# 	log.close()









