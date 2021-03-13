from Block.Block import Block


class Blockchain:
    def __init__(self):
        self.blockchain = [self.createGenesis()]

    def createGenesis(self):
        return Block(0)

    def lastBlock(self):
        return self.blockchain[-1]

    def addBlock(self, block):
        block.previousHash = self.lastBlock().hash
        self.blockchain.append(block)
