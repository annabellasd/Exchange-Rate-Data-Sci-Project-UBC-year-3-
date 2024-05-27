import pandas as pd 
import ccxt

# Create an instance of the ccxt exchange object
exchange = ccxt.binance()

# Define the currency pair to trade
symbol = 'BTC/USDT'

# Define the amount to sell (short)
amount = 0.01
# Place a short trade (sell)
order = exchange.create_order(symbol, 'market', 'sell', amount)

# Print the order response
print(order)
