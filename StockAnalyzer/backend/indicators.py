import pandas as pd

def ma(df, period=5):
    return df["close"].rolling(period).mean()
