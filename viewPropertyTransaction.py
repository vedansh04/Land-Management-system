import json

#User enters the property for which transaction history is requied
#The JSON file is accessed which prints the required output
def print_prop_trans(prop):
    prop = "Property " + prop
    file = open("prop_transactions.json")
    data = json.load(file)
    for j in data["Property_Transactions"][prop]:
        i = list(j.values())
        print("")
        print("Transaction ID: " + str(i[0]))
        print("Property: " + str(i[1]))
        print("Price: " + str(i[2]))
        print("Buyer: " + str(i[3]))
        print("Seller: " + str(i[4]))
        print("Timestamp: " + str(i[5]))
        print("")
    file.close()
