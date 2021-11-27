class Block:
    """
    Block: unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Block - data: {self.data}'

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    ThisImplemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')
blockchain.add_block('three')

print(blockchain)