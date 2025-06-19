import hashlib  # For cryptographic hashing
import time  # For timestamps

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index  # Position of the block in the chain
        self.timestamp = time.time()  # Block creation time
        self.data = data  # Transaction or block data
        self.previous_hash = previous_hash  # Link to the previous block's hash
        self.hash = self.calculate_hash()  # Generate hash for the current block

    def calculate_hash(self):
        # Combine all block components into a single string and hash it
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()  # Generate SHA-256 hash
    
class Blockchain:
    def __init__(self):
        # Initialize the blockchain with the genesis block
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Create the first block in the blockchain with predefined data
        # Index 0, no previous hash since it's the first block
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        # Return the most recent block in the chain
        return self.chain[-1]

    def add_block(self, new_data):
        # Add a new block to the chain
        latest_block = self.get_latest_block()
        new_index = len(self.chain)
        new_hash = latest_block.hash
        # Create a new block linking it to the hash of the latest block
        new_block = Block(new_index, new_data, new_hash)
        self.chain.append(new_block)  # Append the new block to the chain

#import time  # Ensure time is imported to use time.ctime for formatting

def display_blockchain(blockchain):
    # Iterate through each block in the blockchain and print its details
    for block in blockchain.chain:
        print(f"Block {block.index}")
        print(f"Timestamp: {time.ctime(block.timestamp)}")  # Convert timestamp to readable time
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
        print("-" * 40)  # Separator for readability

# Assuming the Blockchain and Block classes have been defined as previously described

# Initialize the blockchain
my_blockchain = Blockchain()

# Add some blocks with transaction data
my_blockchain.add_block("Transaction 1: Alice pays Bob 10 BTC")
my_blockchain.add_block("Transaction 2: Bob pays Charlie 5 BTC")

# Display the blockchain to verify its contents
display_blockchain(my_blockchain)