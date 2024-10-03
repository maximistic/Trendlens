import yfinance as yf
import pandas as pd

# Define the stock symbol (use ticker format)
stock_code = 'IDFC.NS'  # For Reliance Industries on NSE

# Fetch live stock data
live_data = yf.Ticker(stock_code)
current_price = live_data.history(period='1d')  # Get the latest price

print(f"Live price for {stock_code}:")
print(current_price)

# Fetch historical stock data
historical_data = live_data.history(start='2023-10-01', end='2023-10-03')

print(f"\nHistorical data for {stock_code}:")
print(historical_data)
