# Project Name: Books to Scrape - Data Science Assignment

### 1. Project Overview

- **Target Website:** http://books.toscrape.com/
- **Data Fields Extracted:** Book Title, Price
- **Tools Used:** Python, BeautifulSoup, Requests

### 2. Setup Instructions

1. Clone this repo: `git clone [YOUR_GITHUB_LINK_HERE]`
2. Install dependencies: `pip install -r requirements.txt`
3. Run script: `python scraper.py`

### 3. Challenges & Solutions

- **Challenge:** Encountered "Disk Full" errors on the primary drive (C:) during environment setup.
- **Solution:** Successfully migrated the project to Volume D and executed the script via terminal. Additionally, handled shortened titles by extracting the 'title' attribute from the HTML <a> tags to ensure data quality.
