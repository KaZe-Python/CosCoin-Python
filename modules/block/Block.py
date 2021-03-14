import time
import hashlib


class Block:
    def __init__(self, idx: int, timestamp, data: str, previousHash = ""):
        self.id = idx
        self.nonce = 0
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash

        self.datahash = (str(self.id) + str(self.nonce) \
                + str(self.timestamp) + str(self.data) \
                + str(self.previousHash)).encode()

        self.hash = self.calculate_blockHash()

    def calculate_blockHash(self):
        return hashlib.sha256(self.datahash).hexdigest()

    def mine_block(self, difficulty):
        zeros_list = [str(0) for _ in range(difficulty)]

        while(list(self.hash[:difficulty]) != zeros_list):
            self.nonce += 1
            self.hash = self.calculate_blockHash()
        return self.hash


    def __repr__(self):
        return f"##### \n\
                Block ID: {self.id}\n\
                Nonce:    {self.nonce}\n\
                Timestamp: {self.timestamp}\n\
                Data:       {self.data}\n\
                Previous Hash:       {self.previousHash}\n\
                Hash: {self.hash}\n\
                \n#####"
