# scripts/fetch_yahoo_data.py
import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_historical_data(ticker_symbol, save_path):
    """
    Fetches historical data for a given ticker symbol and saves it to a CSV file.
    """
    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)
    
    # Fetch historical data
    historical_data = ticker.history(period="max")
    
    # Save the data to a CSV file
    historical_data.to_csv(save_path)
    print(f"Historical data saved to {save_path}")

def fetch_live_data(ticker_symbol, save_folder):
    """
    Fetches live data for a given ticker symbol and saves it to a CSV file with a timestamp.
    """
    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)
    
    # Fetch live data (delayed by 15 minutes)
    live_data = ticker.history(period="1d", interval="1m")
    
    # Save the data with a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    save_path = f"{save_folder}/sp500_live_{timestamp}.csv"
    live_data.to_csv(save_path)
    print(f"Live data saved to {save_path}")

# Example usage
if __name__ == "__main__":
    ticker_symbol = "^GSPC"
    
    # Fetch historical data
    fetch_historical_data(ticker_symbol, "data/raw/sp500_historical.csv")
    
    # Fetch live data
    fetch_live_data(ticker_symbol, "data/raw")