# simple-blockchain
Simple blockchain using Python and Flask framework.


This program creates a simple blockchain using Python and Flask framework. The blockchain consists of a series of blocks, where each block contains a unique digital fingerprint (hash) and a reference to the previous block.

# Endpoints
The program has three endpoints that can be accessed using HTTP GET method:

/mine_block: Mines a new block and adds it to the blockchain.

/get_chain: Returns the entire blockchain in JSON format.

/valid: Validates the blockchain and returns a message indicating whether the blockchain is valid or not.
