from bs4 import BeautifulSoup
import requests
from csv import writer

def product_printer(products):
    for product in products:
        productName = product.a.get("title")
        productLink = product.a.get("href")

        print(productName)

        try: 
            product_r = requests.get(productLink)
        except:
            print("!!! Not Found !!!")

        product_soup = BeautifulSoup(product_r.text, 'html.parser')
        features = product_soup.find_all("li", attrs={"class": "unf-prop-list-item"})
        for feature in features:
            featureTitle = feature.find("p",attrs={"class":"unf-prop-list-title"}).text
            featureText = feature.find("p",attrs={"class":"unf-prop-list-prop"}).text
            print(featureTitle, " : ", featureText)
        print("#"*10)

for i in range(5):
    base_url = f'https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?pg={i}'
    response = requests.get(base_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all("li",attrs={"class":"column"})
    product_printer(products)