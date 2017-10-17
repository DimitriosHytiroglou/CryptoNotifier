import sys
sys.path.insert(0, '../db')
from TwilioCall import send_er_notification, send_pivot_notification


# Definition of the function that does the check for the Divergence service.
def check_Divergence(coin1, coin2, user_signal, ex_rate, first_name, telephone):


		if ex_rate >= float(user_signal):
			print("Success")
			send_er_notification(coin1, coin2, user_signal, ex_rate, first_name, telephone)
		else:
			pass


# Definition of the function that does the check for the Spike service.
def check_Spike(coin1, user_signal, price, direction, first_name, telephone):

	if direction == 'A':					# If checks the direction of the check needed (Above the given price or below the given price)
		if price >= user_signal:

			send_pivot_notification(coin1, user_signal, price, direction, first_name, telephone)		# If the check is true this calls the notification function 
		else:
			pass

	elif direction == 'B':
		if price <= user_signal:

			send_er_notification(coin1, user_signal, price, direction, first_name, telephone)
		else:
			pass