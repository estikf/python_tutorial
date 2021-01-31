import requests
from bs4 import BeautifulSoup

with open('data.txt','w',encoding='utf-8') as f:

    url = r"https://eksisozluk.com/eksi-sozluk-dertlesecek-insan-veritabani--3188805"

    page = 1

    user_agent = {"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

    for i in range(0, 10):

        request_url = url + '?p=' + str(page)
        r = requests.get(request_url, headers=user_agent)
        soup = BeautifulSoup(r.text, 'html.parser')
        page += 1
        
        for i in range(0, len(soup.find_all('div',class_='content'))):
            entry = str(soup.find_all('div',class_='content')[i])[27:-10]
            yazar =  soup.find_all('a',class_='entry-author')[i].text
            tarih = soup.find_all('a',class_='entry-date permalink')[i].text

            f.writelines(f'\nEntry:{entry} \nYazar:{yazar} \nTarih:{tarih}\n')