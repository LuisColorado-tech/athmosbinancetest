from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_restful import Resource, Api
import json

from models.coin_in_db import Coin
from flask_swagger_ui import get_swaggerui_blueprint



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

# host
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/coin_db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Coin(db.Model):
    __tablename__ = 'coin'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    e = Column(DateTime)
    t = Column(String(50))
    tt = Column(String(50))
    s = Column(String(50))
    i = Column(String(50))
    f = Column(String(50))
    ll = Column(String(50))
    o = Column(String(50))
    c = Column(String(50))
    h = Column(String(50))
    l = Column(String(50))
    v = Column(String(50))
    n = Column(String(50))
    x = Column(String(50))
    q = Column(String(50))
    vv = Column(String(50))
    q = Column(String(50))
    b = Column(String(50))


@app.route('/', methods=['POST'] )
def create():
    if request.method == 'POST':
        data = request.get_json()
        coin = Coin(
            name=data['name'],
            e=data['e'],
            t=data['t'],
            tt=data['tt'],
            s=data['s'],
            i=data['i'],
            f=data['f'],
            ll=data['ll'],
            o=data['o'],
            c=data['c'],
            h=data['h'],
            l=data['l'],
            v=data['v'],
            n=data['n'],
            x=data['x'],
            q=data['q'],
            vv=data['vv'],
            q=data['q'],
            b=data['b']
        )
        db.session.add(coin)
        db.session.commit()
        return make_response(json.dumps({'message': 'Coin created successfully'}), 201)
    elif request.method == 'GET':
        coins = Coin.query.all()
        result = coins_schema.dump(coins)
        return make_response(json.dumps(result.data), 200)

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

