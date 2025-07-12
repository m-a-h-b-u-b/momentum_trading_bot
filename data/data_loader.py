import yfinance as yf
import pandas as pd

def fetch_data(symbol="AAPL", start="2022-01-01", end="2023-01-01"):
    df = yf.download(symbol, start=start, end=end)
    df.dropna(inplace=True)
    return df
