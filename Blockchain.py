from modules.block.Block import Block
from modules.transaction.Transaction import Transaction
import time


class Blockchain:
    def __init__(self):
        self.blockchain = [self.create_genesis()]
        self.difficulty = 0

    @staticmethod
    def create_genesis() -> Block:
        return Block(0,time.time(), "gen", 0)

    def add_block(self, block: Block) -> None:
        block.previousHash = self.get_last_block().hash
        block.hash = block.mine_block(self.difficulty)
        self.blockchain.append(block)

    def is_chain_valid(self) -> bool:
        for idx in range(1,len(self.blockchain)):
            current_block = self.blockchain[idx]
            previous_block = self.blockchain[idx-1]

            if current_block.hash != current_block.calculate_blockHash():
                return False
            
            if current_block.previousHash != previous_block.hash:
                return False

        return True

    def get_last_block(self):
        return self.blockchain[-1]
    
    def print_chain(self):
        for block in self.blockchain:
            print(block)


blockchain = Blockchain()
print("mining block 1")
blockchain.add_block(Block(1, "14/03/2021", {"amount": 4}))

print("mining block 2")
blockchain.add_block(Block(2, "15/03/2021", {"amount": 5}))

blockchain.print_chain()
print(blockchain.is_chain_valid())
