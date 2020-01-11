import requests

from api import app
from api.stock.constants import AlphaVantageStockFunctionEnum


class StockDao:
    stock: dict
    symbol: str
    api_key = app.config['ALPHA_VANTAGE_API_KEY']
    api_function: AlphaVantageStockFunctionEnum = AlphaVantageStockFunctionEnum.TIME_SERIES_MONTHLY
    ALPHA_VANTAGE_URL = 'https://www.alphavantage.co/query?function={0.api_function.value}&symbol={0.symbol}&apikey={' \
                        '0.api_key} '

    def get_from_alpha_vantage(self, symbol):
        self.symbol = symbol
        response = requests.get(self.get_endpoint())
        self.stock = response.json()

    def get_endpoint(self):
        return self.ALPHA_VANTAGE_URL.format(self)
