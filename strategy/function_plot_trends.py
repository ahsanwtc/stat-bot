import matplotlib.pyplot as plt
import pandas as pd
from functions_cointegration import extract_close_prices, calculate_cointegration, calculate_spread, calculate_zscore

def plot_trends(symbol_1, symbol_2, price_data):
    # extract prices
    prices_1 = extract_close_prices(price_data[symbol_1])
    prices_2 = extract_close_prices(price_data[symbol_2])

    # get spread and z-score
    coint_flag, t_value, p_value, c_value, hedge_ratio, zero_crossings = calculate_cointegration(prices_1, prices_2)
    spread = calculate_spread(prices_1, prices_2, hedge_ratio)
    z_score = calculate_zscore(spread)

    # calculate percentage changes
    df = pd.DataFrame(columns=[symbol_1, symbol_2])
    df[symbol_1] = prices_1
    df[symbol_2] = prices_2
    df[f"{symbol_1} pct"] = df[symbol_1] / prices_1[0]
    df[f"{symbol_2} pct"] = df[symbol_2] / prices_2[0]
    series_1 = df[f"{symbol_1} pct"].astype(float).values
    series_2 = df[f"{symbol_2} pct"].astype(float).values

    # save results for back testing
    df_2 = pd.DataFrame()
    df_2[symbol_1] = prices_1
    df_2[symbol_2] = prices_2
    df_2['spread'] = spread
    df_2['Zscore'] = z_score
    df_2.to_csv('03_backtest_file.csv')
    print('file for backtesting saved.')

    # plot charts
    figure, axis = plt.subplots(3, figsize=(16, 8))
    figure.suptitle(f"Price and Spread - {symbol_1} vs {symbol_2}")
    axis[0].plot(series_1)
    axis[0].plot(series_2)
    axis[1].plot(spread)
    axis[2].plot(z_score)
    plt.show()
