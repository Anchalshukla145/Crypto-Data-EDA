# 💰 Crypto Data EDA (Exploratory Data Analysis & Preprocessing)

This project focuses on preparing and analyzing **cryptocurrency market data**.  
It merges multiple raw CSV files into one clean dataset (`Coin.csv`) containing prices, volume, and market capitalization for different cryptocurrencies.  
The cleaned dataset can then be used for further **Exploratory Data Analysis (EDA)** or predictive modeling.

---

## 📂 Project Structure

Crypto-Data-EDA/
│── CryptoSolution.py # Script to merge and clean multiple crypto CSVs

│── Coin.csv # Final merged dataset

│── dataset/ # (Optional) Raw CSVs for different coins

│── requirements.txt # Dependencies list

│── README.md # Project documentation



---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Crypto-Data-EDA.git
   cd Crypto-Data-EDA
Install dependencies:

bash
Copy code
pip install -r requirements.txt
📦 Dependencies
The project requires the following Python libraries:

pandas → Data manipulation & analysis

glob → File searching (to load multiple CSVs)

os → File path operations

(All included in requirements.txt)

▶️ How to Run
Place all your raw crypto CSV files inside the dataset/ folder.

Each file should be named like: coin_Bitcoin.csv, coin_Ethereum.csv, etc.

Each file must include at least: Date, Open, High, Low, Close, Volume, Marketcap

Run the script:

bash
Copy code
python CryptoSolution.py
The merged and cleaned dataset will be saved as:

Copy code
Coin.csv
📊 Output
A single merged CSV file containing all cryptocurrencies

Columns: Date, Symbol, Open, High, Low, Close, Volume, Marketcap

Cleaned data includes:

Removal of missing Date, Symbol, or Close

Proper datetime format

Sorted by Date and Symbol

🚀 Features
✅ Combines multiple crypto datasets into one structured file

✅ Cleans missing values for consistency

✅ Creates a ready-to-use dataset for EDA or ML modeling

✅ Supports multiple coins dynamically (reads all CSVs from folder)

📝 Future Improvements
🔗 Automate data fetching from APIs (e.g., CoinGecko, Binance)

📈 Add exploratory analysis notebooks (price trends, volatility, correlations)

📊 Extend to visualization and dashboards

**📖 Quote**

**"Without data, you're just another person with an opinion." — W. Edwards Deming**
