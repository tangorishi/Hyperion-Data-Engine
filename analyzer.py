import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(filename):
    try:
        df = pd.read_csv(filename)
        print("Data loaded successfully:")
        print(df.head())

        
        num_quotes = len(df)
        plt.figure(figsize=(6, 4))
        plt.bar(['Total Quotes'], [num_quotes], color='skyblue')
        plt.title('Total Number of Quotes Scraped')
        plt.ylabel('Count')
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please run scraper.py first.")

if __name__ == '__main__':
    analyze_data("quotes.csv")