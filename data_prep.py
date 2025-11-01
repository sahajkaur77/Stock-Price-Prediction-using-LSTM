import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def load_data(path="../data/stock_data.csv"):
    """Load stock dataset from CSV (fetched using yfinance)"""
    df = pd.read_csv(path)

    # Make sure Date is parsed and dropped
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.dropna()

    # Ensure we only have numeric Close prices
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df = df.dropna(subset=["Close"])

    return df

def preprocess(df, steps=60):
    """Scale and create sequences for training"""
    data = df['Close'].values.reshape(-1,1)

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    x, y = [], []
    for i in range(steps, len(scaled_data)):
        x.append(scaled_data[i-steps:i, 0])
        y.append(scaled_data[i, 0])

    x, y = np.array(x), np.array(y)
    x = np.reshape(x, (x.shape[0], x.shape[1], 1))
    return x, y, scaler, data
