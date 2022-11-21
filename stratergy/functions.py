from datetime import datetime, timedelta
import time
import json
from config_api import session, timeframe, kline_limit

def get_tradeable_symbols():
    symbol_list = []
    symbols = session.query_symbol()
    if 'ret_msg' in symbols.keys() and symbols['ret_msg'] == 'OK':
        symbols = symbols['result']

    for symbol in symbols:
        if symbol['quote_currency'] == 'USDT' and float(symbol['maker_fee']) < 0.01 and symbol['status'] == 'Trading':
            symbol_list.append(symbol)

    return symbol_list


"""
interval: 60, "D"
from: integer from timestamp in seconds
limit: max size of 200

Get historical prices (klines)
"""
def get_price_klines(symbol):
    time_start_date = 0
    if timeframe == 60:
        time_start_date = datetime.now() - timedelta(hours=kline_limit)
    if timeframe == 'D':
        time_start_date = datetime.now() - timedelta(days=kline_limit)

    time_start_seconds = int(time_start_date.timestamp())

    # Get prices
    prices = session.query_mark_price_kline(
        symbol=symbol,
        interval=timeframe,
        limit=kline_limit,
        from_time=time_start_seconds
    )

    # manage API call limit
    time.sleep(0.1)

    # if not enough data for the token to process
    if len(prices['result']) != kline_limit:
        return []
    return prices['result']


# store price history for all available pairs
def store_price_history(symbols):

    # get prices and store in DataFrame
    counts = 0
    price_history_dictionary = {}
    for symbol in symbols:
        symbol_name = symbol['name']
        price_history = get_price_klines(symbol_name)
        if len(price_history) > 0:
            price_history_dictionary[symbol_name] = price_history
            counts += 1
            print(f"{counts} items stored")
        else:
            print(f"{counts} items not stored")

    # save prices to JSON file
    if len(price_history_dictionary) > 0:
        with open('01_price_list.json', 'w') as fp:
            json.dump(price_history_dictionary, fp, indent=2)
        print('Prices saved successfully.')

    return
