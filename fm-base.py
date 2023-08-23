import requests
from bs4 import BeautifulSoup

url = "https://fminside.net/players"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
site = requests.get(url, headers = headers)

soup = BeautifulSoup(site.content, 'html.parser')

players = soup.find_all('li', class_ = 'player')

for player in players:
    player_info = player.find('span', class_='name')
    if player_info:
        player_name = player_info.find('a').text
        player_link = player_info.find('a')['href']
        player_link_final = f'https://fminside.net{player_link}'
        print(f'nome: {player_name} | link: {player_link_final}')
        
        player_site = requests.get(player_link_final, headers = headers)
        player_soup = BeautifulSoup(player_site.content, 'html.parser')
        print(player_soup)
        print('\n----------------------')