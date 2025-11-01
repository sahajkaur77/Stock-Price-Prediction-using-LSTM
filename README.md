# Stock-Price-Prediction-using-LSTM
This project uses Long Short-Term Memory (LSTM) neural networks to predict future stock prices based on historical data. It demonstrates a complete pipeline — from data fetching to preprocessing, training, prediction, and visualization.

🚀 Features

Fetches real stock market data using yfinance

Preprocesses data with MinMaxScaler

Trains a deep learning model (LSTM) for time-series forecasting

Saves trained model and scaler for future use

Visualizes actual vs predicted stock prices in an interactive graph

🧠 Project Structure
Stock price prediction/
<img width="781" height="519" alt="image" src="https://github.com/user-attachments/assets/8af9e939-55a0-4df8-940a-6f8ee4480eab" />

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/stock-prediction-lstm.git
cd stock-prediction-lstm

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

Example requirements.txt
numpy
pandas
tensorflow
matplotlib
yfinance
scikit-learn
joblib

🧩 Usage
Step 1 — Fetch Data
python src/fetch_data.py

Step 2 — Train the Model
python src/train.py

Step 3 — Make Predictions
python src/predict.py

Step 4 — Visualize Results
python src/visualize.py

📊 Output Example

The model generates a plot comparing Actual vs Predicted Stock Prices:
