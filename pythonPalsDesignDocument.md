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
