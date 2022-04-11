import os
import random
from flask import Flask
from flask_cors import CORS
import requests

from backend.config import PORT, ROOT_PORT

from backend.models.blockchain import Blockchain
from backend.routes.wallet import WALLET
from backend.routes.blockchain import BLOCKCHAIN
from backend.routes.transaction import TRANSACTION

app = Flask(__name__)
@app.route('/')
def route_default():
    return 'Welcome to the blockchain ;)'

app.register_blueprint(BLOCKCHAIN, url_prefix="/blockchain")
app.register_blueprint(TRANSACTION, url_prefix="/transactions")
app.register_blueprint(WALLET, url_prefix="/wallet")

CORS(app, resources={ r'/*': { 'origins' : 'http://localhost:3001'} })

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

    result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
    result_blockchain = Blockchain.from_json(result.json())

    try:
        Blockchain.replace_chain(result_blockchain.chain)
        print('\n -- Succesfully synchronized the local chain')
    except Exception as e:
        print(f'\n --Error synchronizing: {e}')

app.run(host='0.0.0.0', port=PORT, debug=False)