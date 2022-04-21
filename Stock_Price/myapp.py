import yfinance as yf
import streamlit as st

st.header("Stock Price App")

"***"
#GOOGLE Stock Price
st.subheader("GOOGLE")

#define the ticker symbol
tickerSymbol = 'GOOGL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2004-8-14', end='2022-4-1')

# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("**Closing Price**")
st.area_chart(data=tickerDf.Close)
st.write("**Volume**")
st.area_chart(tickerDf.Volume)


"***"
# APPLE Stock Price
st.subheader("APPLE")
tickerSymbol1 = 'AAPL'
tickerData1 = yf.Ticker(tickerSymbol1)
tickerDf1 = tickerData1.history(period='1d', start='1980-12-12', end='2022-4-1')
st.write("**Closing Price**")
st.area_chart(tickerDf1.Close)
st.write("**Volume**")
st.area_chart(tickerDf1.Volume)


"***"
# TESLA Stock Price
st.subheader("TESLA")
tickerSymbol2 = 'TSLA'
tickerData2 = yf.Ticker(tickerSymbol2)
tickerDf2 = tickerData2.history(period='1d', start='1980-12-12', end='2022-4-1')
st.write("**Closing Price**")
st.area_chart(tickerDf2.Close)
st.write("**Volume**")
st.area_chart(tickerDf2.Volume)