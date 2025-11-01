from data_prep import load_data, preprocess
from model import build_model
import os

def train():
    df = load_data()   # <-- this now loads fresh data from fetch_data.py
    x, y, scaler, data = preprocess(df)

    model = build_model((x.shape[1], 1))
    model.fit(x, y, batch_size=32, epochs=10)

    if not os.path.exists("../saved"):
        os.makedirs("../saved")

    model.save("../saved/stock_model.h5")

    import joblib
    joblib.dump(scaler, "../saved/scaler.pkl")

    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train()
