import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.sports-reference.com/cfb/awards/heisman.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table', class_='sortable stats_table')

configurable_titles = ['Name', 'School', 'stats']

if table:
    header_row = [header.text.strip() for header in table.find_all('th') if header.text.strip() != 'Voting']

    with open('PrevWinners.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header_row)

        for row in table.find_all('tr')[1:]:
            data_row = [data.text.strip() for data in row.find_all('td')[1:] if data.text.strip() != 'Voting']

            csv_writer.writerow(data_row)

    print("Scraping and writing to CSV complete. Check 'heisman_data.csv'")
else:
    print("Table with class 'sortable stats_table' not found.")
