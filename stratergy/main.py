import json
import warnings
import pandas as pd
import functions
from functions_cointegration import get_cointegrated_pairs

warnings.simplefilter(action='ignore', category='FutureWarning')


"""
    Strategy Code
"""
if __name__ == "__main__":

    # # Step 1: Get the list of symbols
    # print('Getting symbols...')
    # symbol_response = functions.get_tradeable_symbols()
    #
    # # Step 2: Construct and save price history
    # print('Constructing and saving price data to JSON...')
    # if len(symbol_response) > 0:
    #     functions.store_price_history(symbol_response)

    # Step 3: Find cointegrated pairs
    print('Calculating co-integration...')
    with open('01_price_list.json') as json_file:
        price_data = json.load(json_file)

        if len(price_data) > 0:
            coint_pairs = get_cointegrated_pairs(price_data)
    print('Done')
