import pandas as pd
import yfinance as yf
from datetime import datetime

def __init__(self, data):
    self.data = data

# Download historical data for desired ticker symbol
def download_data(self, stock, start, end):
    data = yf.download(stock, start, end)
    return data

# Calculate the Simple Moving Average
def calculate_SMA(self, data, window):
    sma = data.rolling(window=window).mean()
    return sma

# Create a function to signal when to buy and sell an asset
def generate_signals(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short simple moving average
    signals['short_mavg'] = calculate_SMA(data, short_window)

    # Long simple moving average
    signals['long_mavg'] = calculate_SMA(data, long_window)

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Define the ticker list
tickers = ['AAPL']

# Fetch the data
data = download_data(tickers[0], '2020-01-01', datetime.now().strftime('%Y-%m-%d'))

# Generate signals
signals = generate_signals(data['Close'], 50, 200)

# Print the dataframe
print(signals)