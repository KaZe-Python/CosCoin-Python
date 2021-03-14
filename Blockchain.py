from modules.block.Block import Block
from modules.transaction.Transaction import Transaction


class Blockchain:
    def __init__(self):
        self.blockchain = [self.create_genesis()]

    @staticmethod
    def create_genesis() -> Block:
        return Block(0, 0, "13/03/2021", "genesis", 0000)

    def get_last_block(self) -> Block:
        return self.blockchain[-1]

    def add_block(self, block: Block) -> None:
        block.previousHash = self.get_last_block().hash
        block.hash = block.calculateBlockHash()
        self.blockchain.append(block)

    def is_chain_valid(self) -> bool:
        for idx in range(1,len(self.blockchain)):
            current_block = self.blockchain[idx]
            previous_block = self.blockchain[idx-1]

            if current_block.hash != current_block.calculateBlockHash():
                return False
            
            if current_block.previousHash != previous_block.hash:
                return False

        return True
    
    def print_chain(self):
        for block in self.blockchain:
            print(block)


blockchain = Blockchain()
blockchain.add_block(Block(1, 0, "14/03/2021", {"amount": 4}))
blockchain.add_block(Block(2, 0, "15/03/2021", {"amount": 5}))
print(blockchain.is_chain_valid())