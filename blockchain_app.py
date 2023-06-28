import hashlib
import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(data_string.encode()).hexdigest()


def create_genesis_block():
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")


class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)


# Create a new instance of the blockchain
blockchain = Blockchain()

# Add some blocks to the blockchain
blockchain.add_block(Block(1, datetime.datetime.now(), "Block 1 Data", ""))
blockchain.add_block(Block(2, datetime.datetime.now(), "Block 2 Data", ""))
blockchain.add_block(Block(3, datetime.datetime.now(), "Block 3 Data", ""))
blockchain.add_block(Block(4, datetime.datetime.now(), "Block 4 Data", ""))
blockchain.add_block(Block(5, datetime.datetime.now(), "Block 5 Data", ""))

# Print the blockchain
for block in blockchain.chain:
    print("Block Index:", block.index)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("--------------------")
