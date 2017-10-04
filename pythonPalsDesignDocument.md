# Python Pals
* Joyce S. Lee
* Surya Sendyl
* Dimitris Hytiroglou


# To Hodl Or Not To Hodl
## Problem Statement
Managing financial assets requires rational decision making, but this can be difficult when markets are volatile. **To Hodl Or Not To Hodl** provides real-time, relevant information to cryptocurrency holders to keep users informed of price movements in a timely manner.

## Use Cases
**To Hodl Or Not To Hodl** will send price-movement notifications to users via text message. There are two primary use cases:
1. Users can input the following information, via Terminal:

    * a currency to watch 
    * specified price they’d like to benchmark against (e.g. purchase price)
    * phone number to notify. 

The output will be a notification via text message when the specified currency falls below the benchmark price. 

2. Users can input the following information, via Terminal:

    * 2 currencies to watch (that they expect to have correlated movements) 
    * the amount of divergence at which they expect to be notified 
    * phone number to notify. 

The output will be a notification via text message when the specified currencies diverge the specified amount. Note that the amount of divergence will affect the frequency that the system sends the user notifications. The system may suggest amounts as well, for a better user experience.

## Assumptions and constraints

### Input 
Regarding user input, the necessary checks will be implemented in the code to only allow proper input. Furthermore, appropriate guidelines will be given to the user to help him out.


### Execution

#### User input
It will be possible to add a new user or update an existing one at any point in time through the command line. The users and their data are stored in the Shelve database.

#### Notification
The main python script will be constantly running on a server.
At set intervals the program will:
	1. Retrieve the user objects from the Shelve DB 
	2. Check their variables
	3. Query the CryptoCompare API accordingly
	4. When necessary contact the Twillio API and send out the appropriate notification to the user.

## Architecture
A graphical layout of the whole architecture can be found in the "To Hodl or Not to Hodl.pdf" file.
	* Link to pdf: https://github.com/INFO206-Fall2017/pythonpals/blob/master/To%20Hodl%20or%20Not%20to%20Hodl%20-%20Architecture.pdf
![](https://github.com/INFO206-Fall2017/pythonpals/blob/master/To%20Hodl%20or%20Not%20to%20Hodl%20-%20Architecture.pdf)


The main features of the program are:
1. The main python module
2. A shelves database that stores each users data and notification requirements
3. The CryptoCompare API
4. Twillio API
5. The command line user interface

## Implementation Plan
#### Features:
1. Main python module (hosted on AWS)
2. Shelves database (hosted on AWS)
3. CryptoCompare API to make calls for relevant data
4. Twilio API to send text message notifications based on user specifications
5. Command line interface to input currencies, benchmark or diversion amount, and cell phone number

#### Required Algos/Data Structures for each feature:
1. Data structures to be used: classes, dictionaries, lists. We will also be using for loops and while loops as well to iterate through the various data sctructures. 
2. The shelves database takes objects saved in python and converts them to byte code to be stored. When they are called again they get converted back. This python library makes it easy for us to do this, accepting data of various types including strings, integers and floats.
3. The CryptoCompare API returns data in the form of a JSON dump which then needs to be parsed further. A JSON file is composed for nested dictionaries, with various data types within it. In this specific case, the JSON output contains data in the form of strings for the currency codes and integers for the exchange rate or currency value
4. The Twilio API takes data in the form of strings for the message content and integers for the cell phone numbers. We will be using both of these datatypes for our implementation. 
5. The command line interface will interact with our python scripts and take in data as as string, which will then be converted to an int or float as needed like with the case of cell phone numbers

#### Existing work:
* Each feature will be written by us as there has been no previous implementation like this in the past. For the CryptoCompare and Twilio APIs we will be relying on the provided documentation and examples as a starting point:
	* Twilio API docs: https://www.twilio.com/docs/api/messaging
	* CrpytoCompare API docs: https://www.cryptocompare.com/api/#-api-data-socialstats-

#### Team responsibilities and Estimated dates:
* Team: Dimitrius Hytiroglou (**DH**), Joyce Lee (**JL**), Surya Sendyl (**SS**)
1. Shelves Database
	* Ingesting and storing user data (**DH** - 10/8/17)
2. CrpytoCompare API
	* Benchmarking at a particular price (**SS** - 10/8/17)
	* Exchange rate between 2 currencies (**DH** - 10/8/17)
	* Hosting script on AWS (**DH** - 10/8/17)
3. Twilio API
	* Notify users when benchmark is hit (**SS** - 10/12/17)
	* Notify users when exchange rate divergence is hit (**JL** - 10/12/17)
4. Command line interface
	* Python script to interact with command line (**JL** - 10/15/17)
5. Testing
	* Test application before final due date (**ALL** - 10/17/17)

## Test Plan
#### Test Case 1: Exchange rate divergence is set very low
* This case will allow us to test how our program is able to deal with cases where the exchange rate divergence is met frequently, possibly even multiple times a day. We don’t want to spam the user, as such, we need to be able to deal with cases where a notification message needs to get sent out, but has been preceded by a very recent notification message. In cases like these, we will likely send a summary notification message at the end of the day.

#### Test Case 2: Benchmark is crossed more than once a day
* This case allows us to test how our program is able to deal with cases where the benchmark currency value is set at an amount which is frequently crossed on any given day. Given the volatile nature of crypto assets this is definitely a feasible case. In cases like these, as with the above case, we will likely send out a summary message at the day’s end, to avoid spamming the user. 

#### Test Case 3: Making trades based on our divergence notifications
* The most important test for us will be to see if our underlying thesis about the relatedness of the price of 2 crypto currencies is actually valid. To test this we will actually make trades based on the notifications we receive, while also adjusting the threshold of divergence in exchange rates to test out various cases. 

