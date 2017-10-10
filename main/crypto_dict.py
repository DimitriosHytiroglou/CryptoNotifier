import requests as rqst
import threading
import datetime
import json


def Cryptolog():
	request_string = rqst.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=USD,BTC,BCH,ETH,LTC,LSK,NEO,XRP')
	request_dict = request_string.json()
	
	#log = open("Logs/Crypto_array.txt","a")
	#log.write(str(datetime.datetime.now().time())+' - '+request.text+'\n')
	#log.close()


def Repeater():
    Cryptolog()
    threading.Timer(15, Repeater).start()

# start calling f now and every 60 sec thereafter
Repeater()



