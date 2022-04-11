from flask import Flask
from flask_cors import CORS
from routes.blockchain import BLOCKCHAIN

app = Flask(__name__)
@app.route('/')
def route_default():
    return 'Welcome to the blockchain ;)'

app.register_blueprint(BLOCKCHAIN, url_prefix="/blockchain")

CORS(app, resources={ r'/*': { 'origins' : 'http://localhost:3001'} })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)