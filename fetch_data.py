import yfinance as yf
import os

def download_stock(ticker="AAPL", period="5y", interval="1d"):
    """
    Download stock data from Yahoo Finance and save as CSV.
    
    ticker: Stock symbol (e.g., "AAPL" for Apple, "TSLA" for Tesla, "RELIANCE.NS" for Reliance India)
    period: Time range (e.g., "1y", "5y", "10y", "max")
    interval: Data frequency ("1d", "1wk", "1mo")
    """
    print(f"📥 Downloading {ticker} stock data...")

    df = yf.download(ticker, period=period, interval=interval)

    if not os.path.exists("../data"):
        os.makedirs("../data")

    file_path = f"../data/stock_data.csv"
    df.to_csv(file_path)

    print(f"✅ Data saved to {file_path}")

if __name__ == "__main__":
    # Example: Apple stock, last 5 years
    download_stock("AAPL", "5y", "1d")
