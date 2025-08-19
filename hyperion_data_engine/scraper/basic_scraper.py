import requests
from bs4 import BeautifulSoup
import csv

def scrape_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        data = [quote.get_text() for quote in quotes]
        return data
    else:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
        return None

def save_to_csv(data, filename):
    if data:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Quotes'])
            for item in data:
                writer.writerow([item])
        print(f"Data saved to {filename}")

if __name__ == '__main__':
    url = "http://quotes.toscrape.com"
    quotes_data = scrape_data(url)
    save_to_csv(quotes_data, "quotes.csv")