import sys
sys.path.insert(0, '../db')
from TwilioCall import send_er_notification, send_pivot_notification



def check_Divergence(coin1, coin2, ex_rate, user_signal, first_name, telephone):


		if ex_rate >= float(user_signal):
			print("Success")
			send_er_notification(coin1, coin2, user_signal, first_name, telephone)
		else:
			pass



def check_Spike(coin1, user_signal, price, direction, first_name, telephone):

	if direction == 'A':
		if price >= user_signal:

			send_pivot_notification(coin1, user_signal, price, direction, first_name, telephone)
		else:
			pass

	elif direction == 'B':
		if price <= user_signal:

			send_er_notification(coin1, user_signal, price, direction, first_name, telephone)
		else:
			pass