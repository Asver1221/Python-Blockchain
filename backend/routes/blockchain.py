import os
import random
import requests

from flask import Blueprint, jsonify, request

from models.blockchain import Blockchain

blockchain = Blockchain()

BLOCKCHAIN = Blueprint('BLOCKCHAIN', __name__)

@BLOCKCHAIN.route('/', methods=['GET'])
def default_blockchain_route():
    return jsonify(blockchain.to_json())

@BLOCKCHAIN.route('/range', methods=['GET'])
def asd():
    pass