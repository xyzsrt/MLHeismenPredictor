import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.ncaa.com/stats/football/fbs/current/individual/8"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', class_='stats-wrap')

index_names = ['Rank', 'Name', 'Team', 'Class', 'Position', 'Games', 'PasAtt', 'PassCom', 'Int', 'PassYds', 'PassTD', 'PassEff']

with open('CurrentPlayers.csv', 'w', newline='') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(index_names)

    for result in results:
        td_elements = result.findAll('td')

        row_data = []

        for i, td in enumerate(td_elements):

            index_name = index_names[i % len(index_names)]
            row_data.append(f"{index_name}: {td.contents}")

        csv_writer.writerow(row_data)
