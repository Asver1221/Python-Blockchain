import os
import random

from flask import Blueprint, jsonify
from backend.models.transaction_pool import TransactionPool
from backend.models.transaction import Transaction
from backend.models.wallet import Wallet

transaction_pool = TransactionPool()

TRANSACTION = Blueprint('TRANSACTION', __name__)

@TRANSACTION.route('/', methods=['GET'])
def route_transactions():
    return jsonify(transaction_pool.transaction_data())

if os.environ.get('SEED_DATA') == 'True':
    for i in range(5):
        transaction_pool.set_transaction(
            Transaction(Wallet(), Wallet().address, random.randint(5, 100))
        )
