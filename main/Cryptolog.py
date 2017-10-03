import requests as rqst
import threading
import datetime

def Cryptolog():
	request = rqst.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BCH,USD,EUR')

	log = open("Logs/Cryptolog.txt","a")

	log.write(str(datetime.datetime.now().time())+' - '+request.text+'\n')

	log.close()


def Repeater():
    Cryptolog()
    threading.Timer(15, Repeater).start()

# start calling f now and every 60 sec thereafter
Repeater()