import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
import lxml
import time



client = MongoClient('localhost', 27017)
database = client.les2_2

vacans = input('Какая профессия? ')
search_vacans = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&text='
base_url = 'hh.ru'
vacancy = f'{search_vacans}{vacans}'


USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'



response = requests.get(vacancy, headers={'User-Agent': USER_AGENT})
soup = BeautifulSoup(response.text, 'lxml')
body = soup.html.body
ads = body.findAll('div', attrs={'class': 'vacancy-serp-item', 'data-qa': 'vacancy-serp__vacancy'})

collection = database.hhru

for vacancies in ads:
    #time.sleep(1, 5)
    try:
        salary = vacancies.findAll('div', attrs={'class': 'vacancy-serp-item__compensation'})[0].text
    except IndexError:
        salary = None
    result = {'name': vacancies.find("a").text,
              'link': vacancies.find("a").attrs["href"],
              'salary': salary}
    collection.insert_one(result)

print(1)