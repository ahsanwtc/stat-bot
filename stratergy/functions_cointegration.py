import math
from statsmodels.tsa.stattools import coint
import statsmodels.api as sm
import pandas as pd
import numpy as np

# calculate spread
def calculate_spread(series_1, series_2, hedge_ratio):
    spread = pd.Series(series_1) - (pd.Series(series_2) * hedge_ratio)
    return spread

# calculate co-integration
def calculate_cointegration(series_1, series_2):
    coint_flag = False
    coint_result = coint(series_1, series_2)
    t_value = coint_result[0]  # T-Value
    p_value = coint_result[1]  # P-Value
    critical_value = coint_result[2][1]  # critical value
    model = sm.OLS(series_1, series_2).fit()
    hedge_ratio = model.params[0]
    spread = calculate_spread(series_1, series_2, hedge_ratio)
    zero_crossings = len(np.where(np.diff(np.sign(spread)))[0])
    if p_value < 0.5 and t_value < critical_value:
        coint_flag = True

    return (coint_flag, round(t_value, 2), round(p_value, 2), round(critical_value, 2), round(hedge_ratio, 2), zero_crossings)

# put close prices into a list
def extract_close_prices(prices):
    close_prices = []

    for price_values in prices:
        if math.isnan(price_values['close']):
            return []
        close_prices.append(price_values['close'])

    return close_prices

# calculate cointegrated pairs
def get_cointegrated_pairs(prices):

    # loop through coins and check for co-integration
    coint_pair_list = []
    included_list = []

    for sym_1 in prices.keys():
        # check each coin against first (sym_1)
        for sym_2 in prices.keys():
            if sym_2 != sym_1:

                # get a unique combination id and ensure one off check
                sorted_characters = sorted(sym_1 + sym_2)
                unique = "".join(sorted_characters)
                if unique in included_list:
                    continue

                # get close prices
                series_1 = extract_close_prices(prices[sym_1])
                series_2 = extract_close_prices(prices[sym_2])

                # check for co-integration and add cointegrated pairs
                coint_flag, t_value, p_value, c_value, hedge_ratio, zero_crossings = \
                    calculate_cointegration(series_1, series_2)

                if coint_flag is True:
                    included_list.append(unique)
                    coint_pair_list.append({
                        "sym_1": sym_1,
                        "sym_2": sym_2,
                        "p_value": p_value,
                        "t_value": t_value,
                        "c_value": c_value,
                        "hedge_ratio": hedge_ratio,
                        "zero_crossings": zero_crossings
                    })

    # output results
    df_coint = pd.DataFrame(coint_pair_list)
    df_coint = df_coint.sort_values("zero_crossings", ascending=False)
    df_coint.to_csv('02_cointegrated_pairs.csv')
    return df_coint
