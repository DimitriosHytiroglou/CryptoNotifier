import sys
sys.path.insert(0, '../db')
from TwilioCall import send_er_notification



def check_Divergence(coin1, coin2, ex_rate, user_signal, first_name, telephone):


		if ex_rate <= float(user_signal):
			print("Success")
			send_er_notification(coin1, coin2, user_signal, first_name, telephone)
		else:
			pass



def check_Spike(coin1, coin2, ex_rate, user_signal, direction, first_name, telephone):

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