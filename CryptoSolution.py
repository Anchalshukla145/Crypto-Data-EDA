import pandas as pd
import os
import glob

directory = r"C:\Users\Anchal\Downloads\cryptodata" 

csv_files = glob.glob(os.path.join(directory, "*.csv"))

all_dataframes = []

desired_columns = ['Date', 'Symbol', 'Open', 'High', 'Low', 'Close', 'Volume', 'Marketcap']

for file in csv_files:
    coin_name = os.path.basename(file).replace('coin_', '').split('.')[0]
    df = pd.read_csv(file, usecols=lambda col: col in desired_columns)
    df['Symbol'] = coin_name
    df = df[desired_columns]
    all_dataframes.append(df)


merged_df = pd.concat(all_dataframes, ignore_index=True)


merged_df['Date'] = pd.to_datetime(merged_df['Date'], errors='coerce')


merged_df = merged_df.dropna(subset=['Date', 'Symbol', 'Close'])

merged_df = merged_df.sort_values(by=['Date', 'Symbol']).reset_index(drop=True)


output_file = r'C:\Users\Anchal\Downloads\cryptodata\Coin.csv' 
merged_df.to_csv(output_file, index=False)
print(f"Merged dataset saved to {output_file}")
print(f"Total rows: {len(merged_df)}")
print(f"Coins included: {merged_df['Symbol'].unique()}")
