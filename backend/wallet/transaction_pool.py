class TransactionPool:
    def __init__(self):
        self.transaction_map = {}
    
    def set_transaction(self, transaction):
        """
        Set a transaction in the transaction pool.
        """
        self.transaction_map[transaction.id] = transaction

    def existing_transaction(self, address):
        """
        Find a transaction generated by the adress in the tranasction pool.
        """
        for transaction in self.transaction_map.values():
            if transaction.input['address'] == address:
                return transaction

    def transaction_data(self):
        """
        Return the transactions of the transaction pool represented in their
        json serialized form.
        """
        # lambda transform each transaction from pool to its json form
        return list(map(
                lambda transaction: transaction.to_json(),
                self.transaction_map.values()
        ))