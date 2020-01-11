from flask_restful import Resource, reqparse

from api.stock.daos import StockDao


class Stock(Resource):
    endpoint = '/stock'

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('SYMBOL', type=str, required=True)
        args = parser.parse_args()
        stock = StockDao()
        stock.get_from_alpha_vantage(args['SYMBOL'])
        return stock.stock
