import numpy as np

def calculate_sma(prices, window):
    return prices.rolling(window=window).mean()
