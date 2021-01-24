from bs4 import BeautifulSoup
import requests
from csv import writer, reader

base_url = 'http://quotes.toscrape.com/page/2/'
x = 2
list1 = list(base_url)
list2 = []
list2.append(base_url)
print(list2)
for a in range(8):
	x += 1
	b = str(x)
	list1[32] = b
	base_url = ''.join(list1)
	list2.append(base_url)

with open('quotes.csv', 'w', encoding="utf-8") as my_csv:
	csv_w = writer(my_csv)
	header_list = ['Author', 'Text', 'Link']
	csv_w.writerow(header_list)

	for url in list2:
		response = requests.get(url)
		soup1 = BeautifulSoup(response.text, 'html.parser')
		
		for quote in soup1.select('.quote'):
			text = quote.find(class_='text').get_text()
			author = quote.find(class_='author').get_text()
			link = 'https://quotes.toscrape.com' + quote.find('a')['href']
			csv_w.writerow([author, text, link])

with open('quotes.csv', 'r', encoding="utf-8") as my_csv:
	csv_r = reader(my_csv)
	for row in csv_r:
		print(row)