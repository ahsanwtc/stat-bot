import warnings
import pandas as pd
from get_symbols import get_tradeable_symbols

warnings.simplefilter(action='ignore', category='FutureWarning')


"""
    Strategy Code
"""
if __name__ == "__main__":

    # Step 1: Get the list of symbols
    get_tradeable_symbols()


