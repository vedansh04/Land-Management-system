#This function prints the leftover unverified transactions in an iteration
def viewUnverifiedTransactions(leftover_transactions):
    if len(leftover_transactions) == 0: 
            print("\nNo Unverfied Transactions.")
            return
    
    for unverified_trn in leftover_transactions:
        print("")
        print("Transaction ID: " + str(unverified_trn[0]))
        print("Property: " + str(unverified_trn[1]))
        print("Price: " + str(unverified_trn[2]))
        print("Buyer: " + str(unverified_trn[3]))
        print("Seller: " + str(unverified_trn[4]))
        print("Timestamp: " + str(unverified_trn[5]))
        print("")