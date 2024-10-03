from nsetools import Nse

# Initialize NSE object
nse = Nse()

# Get stock quote
stock_code = 'RELIANCE'  # Example: Reliance Industries
stock_data = nse.get_quote(stock_code)

# Print stock data
print(stock_data)
