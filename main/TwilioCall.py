import sys
sys.path.insert(0, '../db')
from twilio.rest import Client

# ExchangeRate coin data
coin_pair = ["BTC", "ETH"]
exchange_rate = 1.3

# Pivot coin data
coin = ["BTC"]
price = 3942
pivot_point = 4000

# User data
surya_number = "+18184147092"
bitchass_number = "+15103092040"
user1 = "Surya"
user2 = "Bitchass"

# Twilio account SID, auth token
account_sid = "AC9629dc758c9d995440c7b90b5542d86c"
auth_token  = "b13ff78cc4235ddbabcf41decd4269ee"
client = Client(account_sid, auth_token)


# Send exchange rate notification function
def send_er_notification(coin1, coin2, user_signal, first_name, telephone):
	message = client.messages.create(
	    to = telephone,		  #user number
	    from_ = "+17797747983",   # Account Twilio Number
	    body = ("Hey, " + first_name +": the exchange rate between " +
	    		str(coin1) + " and " + str(coin2) +
	    		" just crossed " + str(user_signal)
	    		+ "! " + "TO HODL OR NOT TO HODL???" +
				"Get more info at"))

	print("Sent: ",message.sid)


# Send pivot notification function
def send_pivot_notification(coin1, coin2, user_signal, first_name, telephone, way):

	if way == "below ":

		message = client.messages.create(
			to=telephone,
			from_="+17797747983",  # Account Twilio Number
			body=("Hey, " + first_name + ": the price of " +
				  coin1 + " just went " + way +
			      user_signal + "! "
			  	  + "TO HODL OR NOT TO HODL???"))

	elif way == "above ":

		message = client.messages.create(
	    	to = telephone,
	    	from_ = "+17797747983",   # Account Twilio Number
	    	body = ("Hey, " + first_name + ": the price of " +
	    			coin1 + " just went " + way +
	    			user_signal + "! "
	    			+ "TO HODL OR NOT TO HODL???"))

	print("Sent: ",message.sid)
