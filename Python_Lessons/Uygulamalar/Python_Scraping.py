import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/jobs/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
pages = len(soup.find_all("ul", attrs={"class":"pagination"})[0].find_all("li")) - 2 

for page in range(1, 4):
    pageRequest = requests.get("https://www.python.org/jobs/?page=" + str(page))
    pageSource = BeautifulSoup(pageRequest.content, "html.parser")
    jobs = pageSource.find("div", attrs={"class":"row"}).ol.find_all("li")
    
    for job in jobs:
        name = job.h2.find("a").text
        location = job.find("span", attrs= {"class":"listing-location"}).text
        company = job.find("span", attrs= {"class": "listing-company-name"}).br.next
        print(name, location, company)
        