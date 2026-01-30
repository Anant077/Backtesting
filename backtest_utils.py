import yfinance as yf
import pandas as pd
import numpy as np

def run_backtest(start_date, end_date):
    gold = yf.download("GC=F", start=start_date, end=end_date)

    gold["Return"] = gold["Close"].pct_change()
    gold["Equity"] = (1 + gold["Return"]).cumprod()

    return gold


def calculate_metrics(gold):
    returns = gold["Return"].dropna()

    total_return = gold["Equity"].iloc[-1] - 1
    sharpe = (returns.mean() / returns.std()) * np.sqrt(252)

    drawdown = gold["Equity"] / gold["Equity"].cummax() - 1
    max_dd = drawdown.min()

    return {
        "Total Return": f"{total_return*100:.2f}%",
        "Sharpe Ratio": f"{sharpe:.2f}",
        "Max Drawdown": f"{max_dd*100:.2f}%"
    }
