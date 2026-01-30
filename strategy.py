import yfinance as yf
import pandas as pd

def run_backtest(start, end):
    gold = yf.download("GC=F", start=start, end=end)

    gold['Return'] = gold['Close'].pct_change()
    gold['Equity'] = (1 + gold['Return']).cumprod()

    return gold
