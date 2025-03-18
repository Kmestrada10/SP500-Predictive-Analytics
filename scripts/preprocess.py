# scripts/preprocess.py
import pandas as pd

def preprocess_data(raw_data_path, processed_data_path):
    """
    Cleans and preprocesses raw data, then saves it to a CSV file.
    """
    # Load raw data
    data = pd.read_csv(raw_data_path, index_col="Date", parse_dates=True)
    
    # Clean data
    data.fillna(method='ffill', inplace=True)  # Forward fill missing values
    data.drop_duplicates(inplace=True)  # Remove duplicates
    
    # Feature engineering
    data['SMA_50'] = data['Close'].rolling(window=50).mean()  # 50-day Simple Moving Average
    data['SMA_200'] = data['Close'].rolling(window=200).mean()  # 200-day Simple Moving Average
    
    # Save processed data
    data.to_csv(processed_data_path)
    print(f"Processed data saved to {processed_data_path}")

# Example usage
if __name__ == "__main__":
    raw_data_path = "data/raw/sp500_historical.csv"
    processed_data_path = "data/processed/sp500_processed.csv"
    preprocess_data(raw_data_path, processed_data_path)