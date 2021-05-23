from bs4 import BeautifulSoup
import requests
from csv import writer

base_url = 'http://quotes.toscrape.com/'
response = requests.get(base_url)

soup1 = BeautifulSoup(response.text, 'html.parser')

for quote in soup1.select('.quote'):
    text = quote.find(class_='text').get_text()
    author = quote.find(class_='author').get_text()
    link = base_url + quote.find('a')['href']
    print(author, text, link,'\n-------------------------------')