import requests
import  json

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

github_api_url = 'https://api.github.com/users/ex-pr/'

user_name = 'repos'

response = requests.get(f'{github_api_url}{user_name}', headers={'User-Agent':USER_AGENT})

data = response.json()

#Только названия репозиториев
repos_name = []

for i in data:
    repos_name.append(i['name'])
print(repos_name) #['-python', 'data_mining', 'math-06-06-2019', 'python-data-science-21.04.2019', 'python13.03.2019', 'terver']


#Запись информации о репозиториях
with open("data1.json", "w") as write_file:
    json.dump(data, write_file)
