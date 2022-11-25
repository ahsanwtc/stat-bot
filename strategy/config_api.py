"""
    API Documentation
    https://bybit-exchange.github.io/docs/futuresV2/linear/#t-introduction
"""

# API imports
# from pybit import usdt_perpetual
from pybit import HTTP
from dotenv import load_dotenv
import os

# take environment variables from .env
load_dotenv()

# Config
mode = 'test'
timeframe = 60
kline_limit = 200
z_score_window = 21

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

# Session activation
session = HTTP(api_url)
