import yfinance as yf


ticker = yf.Ticker('TSLA')

tsla_df = ticker.history(period="2020-12-21")
print(tsla_df)
