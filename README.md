# To Hodl or Not To Hodl?

This is a price-movement notification tool for cryptocurrency holders, created by graduate students at the Berkeley School of Information.

## How to Run

1. Clone the repo.
2. Change into the "main" directory.
3. Run the "User_Interface.py" file.

### Profile Set-Up

1. Select "Create new user" from the menu by entering "1".
2. Enter a username and phone number to receive notifications.
3. OptionaL: enter a real name (first and last) for more personalized messages.

### Spike Service

1. Select "Add new service" from the menu by entering "2".
2. Select "Spike Notifications" by entering "2".
3. Enter a cryptocurrency ticker to watch. The program supports the top 20 tickers from CoinMarketCap.com.
4. Enter a target price.

The user will be notified via SMS when the currency moves above or below the specified benchmark price. 

### Divergence Service

1. Select "Add new service" from the menu by entering "2".
2. Select "Divergence Notifications" by entering "1".
2. Enter 2 cryptocurrency tickers to watch. The program supports the top 20 tickers from CoinMarketCap.com.
3. Enter a divergence amount.

The user will be notified via SMS when the specified currencies diverge the specified amount.

## Next Steps

### Stronger Security

* Encryption of database storing users' personal info
* Passwords for user accounts 
* Phone number authentication (to prevent spam)

### Better Data Validation

* Check phone number entries for correct inputs + for existing accounts 
* Unit tests

### More Human UX
* Chatbot: e.g. "Reply STOP" to turn off notifications
* Use timestamps to check for and prevent over-notification
