"""
    API Documentation
    https://bybit-exchange.github.io/docs/futuresV2/linear/#t-introduction
"""

# API imports
from pybit import HTTP
from dotenv import load_dotenv
import os

# take environment variables from .env
load_dotenv()

mode = 'test'
ticker_1 = 'DOTUSDT'
ticker_2 = 'ETCUSDT'
signal_positive_ticker = ticker_2
signal_negative_ticker = ticker_1
rounding_ticker_1 = 3
rounding_ticker_2 =1
quantity_rounding_ticker_1 = 3
quantity_rounding_ticker_2 = 1

limit_order_basis = True  # will ensure positions (except for Close) will be placed on limit based
tradeable_capital_usdt = 2000  # total tradeable capital to be split between bot pairs
stop_loss_fail_safe = 0.15  # stop loss at market order in case of drastic event
signal_trigger_threshold = 1.1  # z-score threshold which determines trade (must be above 0)

timeframe = 60  # make sure matches the strategy
kline_limit = 200  # make sure matches the strategy
z_score_window = 21  # make sure matches the strategy

# Live API
api_key_mainnet = ''
api_secret_mainnet = ''

# Testnet API
api_key_testnet = os.getenv('BYBIT_TESTNET_KEY')
api_secret_testnet = os.getenv('BYBIT_TESTNET_SECRET')

# Selected API
api_key = api_key_testnet if mode == 'test' else api_key_mainnet
api_secret = api_secret_testnet if mode == 'test' else api_secret_mainnet

# Selected urls
api_url = os.getenv('BYBIT_TESTNET_URL') if mode == 'test' else os.getenv('BYBIT_MAINNET_URL')
ws_public_url = os.getenv('BYBIT_TESTNET_PUBLIC_WS') if mode == 'test' else os.getenv('BYBIT_MAINNET_PUBLIC_WS')

# Session activation
session_private = HTTP(api_url)
session_public = HTTP(api_url, api_key=api_key, api_secret=api_secret)
