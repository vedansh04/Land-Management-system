import datetime
import uuid
import json

def inputTransaction(blockchain,leftover_trns):
    input_transactions = leftover_trns #creating a list which already has unverified transactions
    while(True):
        print("\nInput Transaction Details")
        trn_id = str(uuid.uuid1()) #setting transaction id to a random string
        buy_or_sell = input("Do you wish to buy or sell?[b/s] ")
        
        buyer_name = input("Enter Username: ")
        buyer_list = []
        file = open("user_stats.json", "r")
        data = json.loads(file.read())
        for i in data["user_stats"]:
            if(i["username"]==buyer_name):
                buyer_list.append(buyer_name)
        file.close()
        buyers_set = set(buyer_list)
        flag=0
        if buyer_name in buyers_set:  # will check if buyer username is present in the user_stats
            flag=1
            buyer_pass = input("Enter your Password: ")
            file = open("user_stats.json", "r")
            data = json.loads(file.read())
            for i in data["user_stats"]:
                if(i["username"]==buyer_name):
                    x = i["password"]
                    if(x!=buyer_pass):
                        #print("INCORRECT PASSWORD")   #this will check if user has entered correct password or not
                        flag=0
                        break
            file.close()
            check=1
        if(flag==0):
            print("INVALID CREDENTIALS")
        else:
            
            if(buy_or_sell == 'b'):
                prop_name = input("Enter the property you wish to buy: ")
            else:
                prop_name = input("Enter the property you wish to sell: ")
            prop_name = "Property " + prop_name
            file = open("property_stats.json", "r")
            data = json.loads(file.read())
            prop_seller = data[prop_name]["owner"]
            prop_price = data[prop_name]["price"]  #getting the prop_price and prop_seller of the property entered from the property stats
            file.close()

            if(buy_or_sell == 's'):
                if(buyer_name != prop_seller):
                    print("YOU ARE NOT THE OWNER OF THIS PROPERTY")
                    flag=0
                    check = 0   #checking if seller is the ower of property
                else:
                    buyer_name = None
            else:
                if(buyer_name == prop_seller):
                    print("YOU ALREADY OWN THIS PROPERTY")
                    flag=0
                    check=0     #checking if user is not buying the property already owner by him.This will prevent double spending
                
            if(flag==1):
                input_transactions.append((
                trn_id,  #0
                prop_name,  #1
                prop_price, #2
                buyer_name, #3
                prop_seller, #4 
                str(datetime.datetime.now().strftime("%Y-%m-%d AT %H:%M %p")) #5
                ))
        if(check==1 and flag==1):
            import storeTransaction
            storeTransaction.store_data(input_transactions[-1]) #storing transaction related to a property
            storeTransaction.modify_data(input_transactions[-1]) # modifying the user stats and property_stats after a transaction is done
        y_or_n = input("Add more?[y/n]")
        if y_or_n == 'n':
            return input_transactions


def addTransactions(input_transactions,blockchain):
    count = len(input_transactions)
    while count>=4:
        verified_trn_list = tuple(input_transactions[:4]) #storing the 4 transactions in verified trn_list
        input_transactions = input_transactions[4:] #remaining transactions will be stored in this list
        hash = blockchain.merkle_hash(verified_trn_list) #calculating the merkel hash of the transactions that make up a block
        blockchain.mine_block(verified_trn_list,hash) #mining the block by passing list of 4transactions and their merkle hash
        #hash = blockchain.merkle_hash(verified_trn_list)
        blockchain.valid_chain(blockchain.chain) #checking if chain is valid or not
        count = count-4

    return input_transactions