import warnings
import pandas as pd
import functions

warnings.simplefilter(action='ignore', category='FutureWarning')


"""
    Strategy Code
"""
if __name__ == "__main__":

    # Step 1: Get the list of symbols
    print('Getting symbols...')
    symbol_response = functions.get_tradeable_symbols()

    # Step 2: Construct and save price history
    print('Constructing and saving price data to JSON...')
    if len(symbol_response) > 0:
        functions.store_price_history(symbol_response)


