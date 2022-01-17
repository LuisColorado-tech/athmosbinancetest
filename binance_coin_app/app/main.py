from flask import Flask, request, make_response
# from flask_restful import Resource, Api
import json

from models.coin_in_db import Coin
from flask_swagger_ui import get_swaggerui_blueprint

# host
app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/', methods=['POST'] )
def create():
    coin_in = request.get_json()

    coin  = Coin(**coin_in)
    coin.save()

    return make_response(json.dumps(coin.to_dict()), 200)

# @app.route('/', methods=['GET'] )
# def getall():
#     data1 = BTCUSDT.Binance_websocket()
#     data2 = ETHUSDT.Binance_websocket()
#     data3 = DOGEUSDT.Binance_websocket()
#     return json.dumps({data1, data2, data3})

# @app.route('/BTCUSDT' , methods=['GET'])
# def getBTCUSD():
#     data = BTCUSDT.Binance_websocket()
#     return json.dumps(data)

# @app.route('/ETHUSDT' , methods=['GET'])
# def getETHUSD():
#     data = ETHUSDT.Binance_websocket()
#     return json.dumps(data)

# @app.route('/DOGEUSDT' , methods=['GET'])
# def getDOGEUSD():
#     data = DOGEUSDT.Binance_websocket()
#     return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
