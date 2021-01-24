import requests
from bs4 import BeautifulSoup
url = 'https://store.steampowered.com/search/?sort_by=Released_DESC&tags=9&page=2'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
games = soup.find_all('div', attrs={'class':'responsive_search_name_combined'})

for game in games:
    a = game.find('span', attrs={'class':'title'}).text
    b = game.find('div', attrs={'class':'col search_released responsive_secondrow'}).text
    c = game.find('div', attrs={'class':'col search_price_discount_combined responsive_secondrow'}).attrs.get('data-price-final')
    d = float(c)/100
    print('Oyun: {} \n Tarih: {} \n Fiyat: {} TL'.format(a,b,d))
    print('-'*30)


