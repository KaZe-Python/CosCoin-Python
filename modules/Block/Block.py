import time
import hashlib


class Block:
    def __init__(self, idx: int, nonce: int, timestamp, data: str, previousHash):
        self.id = idx
        self.nonce = nonce
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash

        self.datahash = (str(self.id) + str(self.nonce) \
                + str(self.timestamp) + str(self.data) \
                + str(self.previousHash)).encode()

        self.hash = self.calculateBlockHash()

    def calculateBlockHash(self):
        return hashlib.sha256(self.datahash).hexdigest()
