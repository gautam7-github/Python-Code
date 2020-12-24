"""
    GET REAL-TIME PRICE OF ANY STOCK
"""

import yfinance as yf
import sys
import json

stocks = {
    'tesla': 'TSLA',
    'apple': 'AAPL',
    'reliance': 'RELIANCE.NS'
}
cmdArgs = sys.argv
if cmdArgs[1] == "-s":
    ticker = yf.Ticker(stocks.get(cmdArgs[2].lower()))
tsla_df = ticker.history(period="2020-12-21")
print(tsla_df)
