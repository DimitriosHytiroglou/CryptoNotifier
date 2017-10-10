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

# Check rate function
def check_rate(coin1, coin2, ex_rate, user_signal, direction, first_name, telephone, ):

	if direction == 'H':
		if ex_rate <= user_signal:
			way = "above "
			send_er_notification(coin1, coin2, user_signal, first_name, telephone, way)
		else:
			pass

	elif direction == 'L':
		if ex_rate >= user_signal:
			way = "below "
			send_er_notification(coin1, coin2, user_signal, first_name, telephone, way)
		else:
			pass

# Send exchange rate notification function
def send_er_notification(coin1, coin2, user_signal, first_name, telephone):
	message = client.messages.create(
	    to = telephone,		  #user number
	    from_ = "+17797747983",   # Account Twilio Number
	    body = ("Hey, " + first_name +": the exchange rate between " +
	    		str(coin1) + " and " + str(coin2) +
	    		" just crossed " + str(user_signal)
	    		+ "! " + "TO HODL OR NOT TO HODL???"))

	print("Sent: ",message.sid)



# Check rate function
#def check_rate():
#	while exchange_rate <= 1.1:
#		pass
#	else:
#		send_er_notification()

# Send exchange rate notification function
#def send_er_notification():
#	message = client.messages.create(
#	    to = surya_number,
#	    from_ = "+17797747983",   # Account Twilio Number
#	    body = ("Hey, " + user1 +": the exchange rate between " +
#	    		str(coin_pair[0]) + " and " + str(coin_pair[1]) +
#	    		" just crossed " + str(exchange_rate)
#	    		+ "! " + "TO HODL OR NOT TO HODL???"))
#
#	print("Sent: ",message.sid)


# Check pivot function
def check_pivot():
	while price > pivot_point:
		pass
	else:
		send_pivot_notification()

# Send pivot notification function
def send_pivot_notification():
	message = client.messages.create(
	    to = surya_number,
	    from_ = "+17797747983",   # Account Twilio Number
	    body = ("Hey, " + user1 + ": the price of " +
	    		str(coin[0]) + " just went below " +
	    		str(pivot_point) + "! " 
	    		+ "TO HODL OR NOT TO HODL???"))

	print("Sent: ",message.sid)


# Main function
def main():
	check_rate()
	check_pivot()

#main()
