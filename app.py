import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Gold Trading Strategy Backtest")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date")
with col2:
    end_date = st.date_input("End Date")

if st.button("Run Backtest"):
    gold = yf.download("GC=F", start=start_date, end=end_date)

    gold["Return"] = gold["Close"].pct_change()
    gold["Equity"] = (1 + gold["Return"]).cumprod()

    fig, ax = plt.subplots()
    ax.plot(gold.index, gold["Equity"])
    ax.set_title("Equity Curve")

    st.pyplot(fig)
    st.write(gold.tail())
