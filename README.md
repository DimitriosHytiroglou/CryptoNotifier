# To Hodl or Not To Hodl?
### Dimitrios Hytiroglou, Surya Sendyl, Joyce Lee

This is a price-movement notification tool for cryptocurrency holders, created by graduate students at the Berkeley School of Information.

## What's "Hodl"?
https://www.reddit.com/r/Bitcoin/comments/2b8t78/whats_hodl/

## How to Run

### 1. Setup
Clone the repo either on your personal machine or a server.

A server is recommended because the script needs to be continuously running.

Make sure you have python3.x installed on the machine and also the following packages:
- requests
- twilio
- shelve
- threading

The very first time you use the program make sure to delete all the *.bak, *.dat, *.dir files in the /db directory.
Then run initializedb.py. This initializes the databases and is needed only the first time the program is run, or when the database is wiped.

### 2. User interface
In the /main directory run User_Interface.py
This brings up the user interface from where you create users and add services to them.

#### Profile Set-Up

1. Select "Create new user" from the menu by entering "1".
2. Enter a username and phone number to receive notifications.
3. Optional: enter a real name (first and last) for more personalized messages.

#### Spike Service

1. Select "Add new service" from the menu by entering "2".
2. Select "Spike Notifications" by entering "2".
3. Enter a cryptocurrency ticker to watch. The program supports the top 20 tickers from CoinMarketCap.com.
4. Enter a target price.

The user will be notified via SMS when the currency moves above or below the specified benchmark price. 

#### Divergence Service

1. Select "Add new service" from the menu by entering "2".
2. Select "Divergence Notifications" by entering "1".
2. Enter 2 cryptocurrency tickers to watch. The program supports the top 20 tickers from CoinMarketCap.com.
3. Enter a divergence amount, which is indicated byy the exchange rate of the 2 coins.

The user will be notified via SMS when the specified currencies diverge by the specified amount.

### 3. Running the notification script

Run main.py for testing purposes.

OR

Run main_loop.py for regular use.
In order to run the service and leave it running on an online server use the command:
"sudo nohup python3 main_loop.py &" 

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
