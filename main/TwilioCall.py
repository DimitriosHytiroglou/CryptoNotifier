import sys
sys.path.insert(0, '../db')
from twilio.rest import Client

# ExchangeRate coin data        ##TO BE REMOVED
coin_pair = ["BTC", "ETH"]      ##TO BE REMOVED
exchange_rate = 1.3             ##TO BE REMOVED

# Pivot coin data               ##TO BE REMOVED
coin = ["BTC"]                  ##TO BE REMOVED
price = 3942                    ##TO BE REMOVED
pivot_point = 4000              ##TO BE REMOVED

# User data                                 ##TO BE REMOVED
surya_number = "+18184147092"               ##TO BE REMOVED
bitchass_number = "+15103092040"            ##TO BE REMOVED
user1 = "Surya"                             ##TO BE REMOVED
user2 = "Bitchass"                          ##TO BE REMOVED

# Twilio account SID, auth token
account_sid = "AC9629dc758c9d995440c7b90b5542d86c"
auth_token  = "b13ff78cc4235ddbabcf41decd4269ee"
client = Client(account_sid, auth_token)


# Send exchange rate notification function
def send_er_notification(coin1, coin2, user_signal, ex_rate, first_name, telephone):
	message = client.messages.create(
	    to = telephone,		  #user number
	    from_ = "+17797747983",   # Account Twilio Number
	    body = ("Hey " + first_name + ", the exchange rate you specified has been crossed! " +
				"Current exchange rate: 1 " +
	    		str(coin1) + " = " + str(format(ex_rate, '.2f')) + " " + str(coin2) +
	    		"! " + "TO HODL OR NOT TO HODL???" +
				" Get more info at https://coinmarketcap.com/"))

	print("Sent: ",message.sid)


# Send pivot notification function
def send_pivot_notification(coin1, user_signal, price, direction, first_name, telephone):

	if direction == "B":

		message = client.messages.create(
			to=telephone,
			from_="+17797747983",  # Account Twilio Number
			body=("Hey " + first_name + ", the price of " +
				  str(coin1) + " just went below $" +
			      str(format(user_signal, '.2f')) + " and is now at $" + str(format(price, '.2f')) + "! "
			  	  + "TO HODL OR NOT TO HODL???" +
				  " Get more info at https://coinmarketcap.com/"))

	elif direction == "A":

		message = client.messages.create(
	    	to = telephone,
	    	from_ = "+17797747983",   # Account Twilio Number
	    	body = ("Hey " + first_name + ", the price of " +
	    			str(coin1) + " just went above $" +
	    			str(format(user_signal, '.2f')) + " and is now at $" + str(format(price, '.2f')) + "! "
	    			+ "TO HODL OR NOT TO HODL???"+
					" Get more info at https://coinmarketcap.com/"))

	print("Sent: ",message.sid)