from data_prep import load_data, preprocess
import matplotlib.pyplot as plt
import numpy as np
import joblib
from tensorflow.keras.models import load_model

def predict():
    df = load_data()
    x, y, scaler, data = preprocess(df)

    # Load model & scaler
    model = load_model("../saved/stock_model.h5")
    scaler = joblib.load("../saved/scaler.pkl")

    # Make predictions
    predictions = model.predict(x)
    predictions = scaler.inverse_transform(predictions)

    # Plot results
    plt.figure(figsize=(14,6))
    plt.plot(data, label="Real Price")
    plt.plot(range(60, 60+len(predictions)), predictions, label="Predicted Price")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    predict()
from src.data_prep import load_data, preprocess
import matplotlib.pyplot as plt
import numpy as np
import joblib
from tensorflow.keras.models import load_model

def predict():
    df = load_data()
    x, y, scaler, data = preprocess(df)

    # Load model & scaler
    model = load_model("../saved/stock_model.h5")
    scaler = joblib.load("../saved/scaler.pkl")

    # Make predictions
    predictions = model.predict(x)
    predictions = scaler.inverse_transform(predictions)

    # Plot results
    plt.figure(figsize=(14,6))
    plt.plot(data, label="Real Price")
    plt.plot(range(60, 60+len(predictions)), predictions, label="Predicted Price")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    predict()
