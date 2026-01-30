import streamlit as st
from strategy import run_backtest

st.title("Gold Trading Strategy Backtest")


start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# BUTTON
if st.button("Run Backtest"):
    df = run_backtest(start_date, end_date)

    st.subheader("Equity Curve")
    st.line_chart(df["Equity"])

    st.subheader("Last Rows")
    st.dataframe(df.tail())
