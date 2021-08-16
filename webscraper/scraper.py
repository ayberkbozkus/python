from bs4 import BeautifulSoup
import requests
from csv import writer

base_url = 'https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu'
response = requests.get(base_url)

soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all("li",attrs={"class":"column"})

for product in products:
    productName = product.a.get("title")
    productLink = product.a.get("href")
    
    try: 
        product_r = requests.get(productLink)
    except:
        print("!!! Not Found !!!")

    product_soup = BeautifulSoup(product_r.text)
    features = product_soup.find_all("div", attrs={"class": "unf-prop"})
    for feature in features:
        print(productName)
        print(feature.find("p",attrs={"class":"unf-prop-list-title"}).text)
        print(feature.find("p",attrs={"class":"unf-prop-list-prop"}).text)
    print("#"*10)