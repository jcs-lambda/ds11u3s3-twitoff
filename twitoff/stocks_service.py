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


request_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=5min&apikey={ALPHAVANTAGE_KEY}'
print(request_url)

response = requests.get(request_url)
print(type(response))
print(response.status_code)
print(response.text)

data = json.loads(response.text)
print(type(data))
print(data.keys())

