import requests
from bs4 import BeautifulSoup
import csv
import time
import os

def start_scraping():
    url = "http://books.toscrape.com/"
    
    # Adding a header to look like a real browser
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    print(f"Connecting to {url}...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Connected successfully!")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Finding all book containers
        books = soup.find_all('article', class_='product_pod')
        print(f"Found {len(books)} books.")
        
        data_list = []
        for book in books:
            # Get Title
            title = book.h3.a['title']
            # Get Price
            price = book.find('p', class_='price_color').text
            
            data_list.append([title, price])
            print(f"Scraped: {title}")

        # Saving to Volume D specifically
        file_path = 'data.csv'
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Book Title', 'Price'])
            writer.writerows(data_list)
        
        # Confirming file size
        if os.path.getsize(file_path) > 0:
            print(f"Success! '{file_path}' is now saved with data.")
        else:
            print("Error: File was created but it is still empty.")
    else:
        print(f"Failed to connect. Status code: {response.status_code}")

if __name__ == "__main__":
    start_scraping()
    time.sleep(1)