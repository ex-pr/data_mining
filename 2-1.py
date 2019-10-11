import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
import lxml
import time


client = MongoClient('localhost', 27017)
database = client.les2_1

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

def req_ads(url):
    response = requests.get(url, headers={'User-Agent': USER_AGENT})
    soup = BeautifulSoup(response.text, 'lxml')
    item = soup.body.findAll('div', attrs={'class': 'seller-info-name'})[0]
    try:
        price = soup.body.findAll('span', attrs={'class': 'js-item-price', 'itemprop': 'price'})[0].attrs.get('content')
    except IndexError:
        price = None
    result = {'url': response.url,
              'price': int(price) if price and price.isdigit else None,
              'name': item.text,
              'name_link': f'{base_url}{item.find("a").attrs["href"]}',
              'params': [tuple(p.text.split(':')) for p in soup.body.findAll('li', attrs={'class': 'item-params-list-item'})]
              }
    return result

base_url = 'https://www.avito.ru'
url = 'https://www.avito.ru/tolyatti/kvartiry/prodam'

response = requests.get(url, headers={'User-Agent': USER_AGENT})
soup = BeautifulSoup(response.text, 'lxml')
body = soup.html.body
ads = body.findAll('div', attrs={'data-marker': 'item'})
urls = [f'{base_url}{itm.find("a").attrs["href"]}' for itm in ads]

collection = database.avito

for itm in urls:
#    time.sleep(1, 5)
    result = req_ads(itm)
    collection.insert_one(result)

print(1)