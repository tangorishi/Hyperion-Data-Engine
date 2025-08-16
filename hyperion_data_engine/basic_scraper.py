import requests
from bs4 import BeautifulSoup
import csv

def scrape_and_save(url, filename, class_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        data_to_scrape = soup.find_all('div', class_=class_name)
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Extracted Data'])
            for data in data_to_scrape:
                writer.writerow([data.get_text(strip=True)])
        
        print(f"Data successfully scraped and saved to {filename}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == '__main__':
    target_url = "https://www.example.com"
    output_filename = "scraped_data.csv"
    target_class = "content-box"
    
    scrape_and_save(target_url, output_filename, target_class)