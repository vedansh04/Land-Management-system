LAND MANAGEMENT SYSTEM

CONTENT OF THE FILE

*Files Included
*Requirements to be Installed
*Project Description
*Function Details
*Steps to run the program
Files included: 
index.py, register.py, BlockChain.py, addTransaction.py, storeTransaction.py, viewBlockchain.py, viewPropertyTransaction.py, view_unverified_transactions.py
Requirements to be installed: 
Programming Language Used: Python (Version: 3.9),
JSON as a NoSQL database

Project Description:
This Project aims at efficient and secure handling of property. This data needs to be secured, because the loss of any such data, or unauthorized access to it may cause a breach in the details of land ownership. 

This problem can be handled using Blockchain Technology, to ensure security and privacy of data. 

•	Transaction will consist of Property details namely:


•	Transaction ID
•	Property name
•	Property price
•	Buyer Name
•	Seller Name
•	Timestamp

•	Only authorized entities, stakeholders can create a transaction pertaining to property and add a block to the blockchain, and access the data.
•	No other person is allowed to access the information.
•	The Node with the maximum number of votes performs delegated proof of stake to verify the transaction.
•	If validation is successful, the block will be added to the blockchain  



Function Details:

1.	Register User: It stores data in a json file containing the information (username, user password, Property Owned by him or not) of the user. Without registration, one cannot buy or sell property.

2.	Add Transaction: This function takes transaction details (user name, user password, Property Name) from the user and check whether the details are valid or not. After the verification it adds the transaction to the block. 4 transactions make up a block.

3.	View Transaction History of Property: It takes the input from the user of the property whose transaction history is required and then prints all the transaction related to that property

4.	View Block: It allows the user to see any block contained in the blockchain.

5.	View Blockchain: It prints the entire blockchain.

6.	View Unverified Transactions: It prints the transactions which have not been included in a block yet.

7.	Exit: It helps the user to exit the system.





Steps to Run the Program:
1)	Execute python files index.py 

2)	Register with a username and password.

3)	To buy or sell properties, use these credentials 

4)	To create a block, a minimum of 4 transactions are required.

5)	In the terminal, a user can view the transactions related to a particular property, the complete blockchain, an individual block of the blockchain, and the unverified transactions.




 
