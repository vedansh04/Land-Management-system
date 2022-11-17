import json

def write_json_user(new_data, prop, filename='prop_transactions.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["Property_Transactions"][prop].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def update_json_property(new_data, prop):
    with open("property_stats.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data[prop]["owner"] = new_data
    price = data[prop]["price"]
    data[prop]["price"] = 1.1*price   #price is increased by 10% every time a transaction is done
    with open("property_stats.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)

def update_json_user(buyer_name, seller_name, new_data):
    prop = new_data[-1]
    with open("user_stats.json", "r") as jsonFile:
        data = json.load(jsonFile)
    
    for i in data["user_stats"]:
        if(i["username"] == seller_name):   #updating the user stats after a transaction
            if(i["properties_owned"]!=None):
                i["properties_owned"] = i["properties_owned"].replace(prop,"")
        if(i["username"] == buyer_name):
            if(i["properties_owned"]!=None):
                i["properties_owned"] = i["properties_owned"] + prop
            else:
                i["properties_owned"] = prop

    with open("user_stats.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)

#To store the transaction details in prop_transactions.json This file is used 
#to store the transaction details of each property.
def store_data(tr_list):
    #for i in range(1):
    m = tr_list[1]
    new_data = {
                "Transaction ID": tr_list[0],
                "Property": tr_list[1],
                "Price":tr_list[2],
                "Buyer Name":tr_list[3],
                "Seller Name":tr_list[4],
                "Timestamp": tr_list[5],
                }
    write_json_user(new_data,m)

#This function is used to update the property owners in user_stats.json and the
#property_stats.json file.  With each transaction, the price of the that property is 
#increased by 10%
def modify_data(tr_list):
    #for i in range (1):
    prop = str(tr_list[1])
    update_json_property(tr_list[3],prop) #change owner in prop
    update_json_user(tr_list[3], tr_list[4], prop)
