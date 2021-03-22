import yfinance as yf

slack = yf.Ticker("WORK")

history = slack.history(period='max')

print(type(history))
print(history.to_csv())
print(history)