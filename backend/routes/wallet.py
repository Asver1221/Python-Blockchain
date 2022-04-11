from flask import Blueprint, jsonify, request

from backend.models.blockchain import Blockchain
from backend.models.transaction import Transaction
from backend.models.transaction_pool import TransactionPool
from backend.models.wallet import Wallet
from backend.pubsub import PubSub

blockchain = Blockchain()
wallet = Wallet(blockchain)
transaction_pool = TransactionPool()
pubsub = PubSub(blockchain, transaction_pool)

WALLET = Blueprint('WALLET', __name__)

@WALLET.route('/info', methods=['GET'])
def route_wallet_info():
    return jsonify({ 'address' : wallet.address, 'balance' : wallet.balance})

@WALLET.route('/transact', methods=['POST'])
def route_wallet_transact():
    transaction_data = request.get_json()
    transaction = transaction_pool.existing_transaction(wallet.address)

    if transaction:
        transaction.update(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )
    else:
        transaction = Transaction(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )

    PubSub.broadcast_transaction(transaction)

    return jsonify(transaction.to_json())
