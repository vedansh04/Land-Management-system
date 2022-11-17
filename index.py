import BlockChain
import viewBlockchain
import AddTransactions 
import register
import viewPropertyTransaction
import json
from random import randint
import view_unverfied_transactions

#to empty property_stats.json
with open("default_property_stats.json", "r") as initial, open("property_stats.json", "w") as final:
    final.write(initial.read()) # This will copy all data from default property_stats to property_stats

#initializing the price of each property as a random integer between 300 and 700
with open("property_stats.json", "r") as jsonFile:
    data = json.load(jsonFile) #data is a dictionary of properties
for prop in data:
    data[prop]["price"] = randint(300,700)
with open("property_stats.json", "w") as jsonFile:
    json.dump(data, jsonFile, indent=4)

#to empty user_stats.json and prop_transactions.json
with open("default_user_stats.json", "r") as initial, open("user_stats.json", "w") as final:
    final.write(initial.read()) 
with open("default_prop_trans.json", "r") as initial, open("prop_transactions.json", "w") as final:
    final.write(initial.read()) #will copy data from default_stats to original file everytime we run the program .
    


blockchain = BlockChain.Blockchain() #will give access to class of blockchain
print("<------------------------SESSION START------------------------->")
leftover_trns = []  #list of leftover_trns not present in the block

while True:
    print("\n_________________________________________")
    print("_________________________________________")
    print("\n[1] - Register User")
    print("[2] - Add Transactions")
    print("[3] - View transaction history of property")
    print("[4] - View a single block")
    print("[5] - View the blockchain")
    print("[6] - View unverified transactions")
    print("\n[e] - Exit")
    choice = input("\n>>> Choose a query to execute: ")

    if choice == "2": 
        unverified_trns = AddTransactions.inputTransaction( blockchain, leftover_trns ) # we will take input of new transaction and add them to the list of leftover_trns
        leftover_trns = AddTransactions.addTransactions( unverified_trns, blockchain )
        # Unverified transactions that weren't added to the block after an iteration 
        # are stored in this list (leftover_trns) and are passed into the next iteration, if there is one. 
        
    elif choice == "1":
        register.register_users()

    elif choice == "3":
        viewPropertyTransaction.print_prop_trans(input("Enter the property for which transaction history is required: "))

    elif choice == "4":
        viewBlockchain.viewBlock(blockchain)
        
    elif choice == "5":
        viewBlockchain.viewBlockchain(blockchain)
    
    elif choice == "6":
        view_unverfied_transactions.viewUnverifiedTransactions(leftover_trns)

    elif choice == "e":
        if(len(list(blockchain.chain))>0):
            if blockchain.valid_chain( blockchain.chain ) == False:
                print("Integrity of blockchain lost!!!")
                exit()

        print("\nThank You for using our Land Management System\n")
        break

    else:
        print('\nPlease choose from the queries given!!!')

print("<-------------------------SESSION END-------------------------->")