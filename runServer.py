from flask import Flask, request

import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/start')
def start():
    return {"status": True}


@app.route('/stop')
def stop():
    return {"status": False}


@app.route('/save', methods=['POST'])
def save_settings():
    data = json.loads(request.data)
    print(data)
    return {"status": True}


@app.route('/profit', methods=['POST'])
def info_profit():
    data = json.loads(request.data)
    print('exchange:', data['exchange'])
    return {
        "symbols": [
            {"name": "INR", "value": 1025},
            {"name": "BTC", "value": 2020},
            {"name": "USDT", "value": 709}
        ]}


@app.route('/balances', methods=['POST'])
def info_balances():
    data = json.loads(request.data)
    # print('exchange:', data['exchange'])
    return {
        "symbols": [
            {"name": "INR", "value": 1025},
            {"name": "BTC", "value": 2020},
            {"name": "USDT", "value": 709}
        ]}


@app.route('/rates')
def rates():
    data = [
        {
            "exchange": "Wazirx",
            "symbol": "XBT/USDT",
            "bid": 0.23424,
            "ask": 0.24803
        },
        {
            "exchange": "Wazirx",
            "symbol": "XBT/USDT",
            "bid": 0.23424,
            "ask": 0.24803
        },
        {
            "exchange": "Wazirx",
            "symbol": "XBT/USDT",
            "bid": 0.23424,
            "ask": 0.24803
        },
        {
            "exchange": "Wazirx",
            "symbol": "XBT/USDT",
            "bid": 0.23424,
            "ask": 0.24803
        }]
    return {"rates": data}


@app.route('/getSettings')
def get_settings():
    settings = {
        "minAmount": 0.01,
        "minDiff": 0.01,
        "symbols": ["BTC/USDT", "ETH/USDT", "XRP/USDT"],
        "wazirxApiKey": "",
        "wazirxSecretKey": "",
        "zebpayApiKey": "",
        "zebpaySecretKey": "",
        "bitbnsApiKey": "",
        "bitbnsSecretKey": "",
        "coindcxApiKey": "",
        "coindcxSecretKey": ""}
    print('get settings', settings)
    return settings


if __name__ == '__main__':
    app.run(debug=True)
