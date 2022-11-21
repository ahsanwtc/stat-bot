from config_api import session

def get_tradeable_symbols():
    symbol_list = []
    symbols = session.query_symbol()
    if 'ret_msg' in symbols.keys() and symbols['ret_msg'] == 'OK':
        symbols = symbols['result']

    for symbol in symbols:
        if symbol['quote_currency'] == 'USDT' and float(symbol['maker_fee']) < 0.01 and symbol['status'] == 'Trading':
            symbol_list.append(symbol)

    return symbol_list
