import hashlib
import json
from random import randint

class Blockchain:
    def __init__(self):
        self.chain = ()
        self.nodes = []
        self.vote_strength = []
        self.votes = []
    
    # A block contains 4 transactions. This function is used to store the transactions and block header details and make a new block.
    def create_block(self, previous_hash, proof_of_delegated_stake, tr_list, hash):
        block = {'Index': len(self.chain) + 1,
                 'Previous Hash': previous_hash,
                 'DPoS': proof_of_delegated_stake,
                 'Merkle Root Hash': hash,
                 'Transactions': tr_list
                }
        temp_list = list(self.chain) #converting tuple to list to add a block
        temp_list.append( block )
        self.chain = tuple(temp_list)  #after block is added chain is again converted to tuple so that immutability of the chain is maintained
        return block
    
    def latest_block(self):
        return self.chain[-1] # this returns last block in the chain

    # to calculate the hash of the contents of a block
    def hash(self, block):
        encoded_block = json.dumps(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

# chain is valid only if the hash of a block is the same as the recalculated hash of the previous hash
    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1
        while(current_index<len(chain)):
            block = chain[current_index]
            #If the hash value of the current block isn't correct then return false
            if(block['Previous Hash']) != self.hash(last_block):
                return False
            last_block = block
            current_index += 1
        return True

 # This function is used to implement the DPoS algorithm. We define the vote strength of each user as the
 # sum total of the price of the properties owned by them. Then each user votes for another user at random 
 # and each user is only allowed one vote. The user who gets the maximum amount of votes validates the block.
 # The maximum number of votes is returned .
    def proof_of_delegated_stake(self):
        file = open("user_stats.json", "r")
        data = json.loads(file.read())
        for i in data["user_stats"]:
            self.nodes.append(i["username"])  #storing all users in self.node
            propstr = i["properties_owned"]
            stakes = len(propstr)   
            price = 0
            self.vote_strength.append(price)
            for j in range(stakes):
                new_file = open("property_stats.json")
                new_data = json.loads(new_file.read())
                new_prop = "Property " + propstr[j]
                price += int(new_data[new_prop]["price"])
                self.vote_strength[-1] = price   #storing the vote strength of a user in self.vote_strength in the same index corresponding to its name in self.node
                new_file.close()
        file.close()
        for i in range(len(self.nodes)):
            self.votes.append(0)

        for i in range(len(self.vote_strength)):
            n = randint(0,len(self.nodes)-1)     #voting is done at random where vote of each person is equal to it's vote strength
            self.votes[n] += self.vote_strength[i]
        self.votes.sort(reverse=True) 
        return self.votes[0]  #returning the maximum number of votes

# This function is used to calculate the Merkle Root Hash of all transactions in a block.
# The transaction ID of all the transaction ID is hashed using SHA 256 and then combined in 
# a specific manner so to get the combined hash of all the transactions.
    def merkle_hash(self,tr_list):
        transactions = []
        transactions.append(tr_list[0][0])  #storing all transactions
        transactions.append(tr_list[1][0])
        transactions.append(tr_list[2][0])
        transactions.append(tr_list[3][0])
        hash1 = []  
        for i in range(4):  #hasing all transactions
            hash1.append(hashlib.sha256(str(transactions[i]).encode()).hexdigest())

        hash2 = []
        hash2.append(hash1[0]+hash1[1])  #combining hashes and hashing their sum
        hash2.append(hash1[2]+hash1[3])
        hash2[0] = hashlib.sha256(str(hash2[0]).encode()).hexdigest()
        hash2[1] = hashlib.sha256(str(hash2[1]).encode()).hexdigest()

        hash = hashlib.sha256((hash2[0]+hash2[1]).encode()).hexdigest() #combining hashes and hashing their sum to get the merkle root hash
        return hash
        
# This function is used to call functions to calculate hash of previous block and find
# the DPoS output. This function then calls the function to create a block
    def mine_block(self,tr_list,hash):
        if len(self.chain)==0:
            previous_hash = self.hash('Genesis Block') #we are hashing the string genesis block to store previous hash in genesis block as no previous block to genesis block exists
            proof_of_delegated_stake = 1 * randint(0,100) 
        else:
            previous_hash = self.hash(self.latest_block())
            proof_of_delegated_stake = self.proof_of_delegated_stake()
        self.create_block(previous_hash, proof_of_delegated_stake, tr_list, hash)