import yfinance as yf

stock = yf.Ticker("^GSPC")

# get historical market data
hist = stock.history(period="max")

hist.to_csv("data.csv")