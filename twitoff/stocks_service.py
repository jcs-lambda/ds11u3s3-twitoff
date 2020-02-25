"""Stocks service.

Stock market data from alphavantage.co

https://www.alphavantage.co/documentation/#daily
"""

import json
import os

import requests
from dotenv import load_dotenv

# establish environment
assert load_dotenv(), 'failed to initialize environment'
ALPHAVANTAGE_KEY = os.getenv('ALPHAVANTAGE_KEY')
assert ALPHAVANTAGE_KEY is not None, \
    'falied to load ALPHAVANTAGE_KEY from environment'


def get_symbol_data(symbol: str = 'TSLA'):
    """Returns dict of the json data returned for symbol."""
    request_url = 'https://www.alphavantage.co/query'
    request_url += '?function=TIME_SERIES_INTRADAY'
    request_url += f'&symbol={symbol}&interval=5min'
    request_url += f'&apikey={ALPHAVANTAGE_KEY}'
    with requests.get(request_url) as r:
        if r.status_code != 200:
            return r.status_code
        return json.loads(r.text)


if __name__ == '__main__':
    data = get_symbol_data()
    print(data)
    print(data.keys())
