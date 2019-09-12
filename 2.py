import requests
import json

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'), headers={'User-Agent':USER_AGENT})

print(response.json()) #{'authenticated': True, 'user': 'user'}
print(response.status_code) #200

api_url = 'https://httpbin.org/get'
r =requests.get(api_url, headers={'User-Agent':USER_AGENT})

data = r.json()

print(data) #{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'},
# 'origin': '74.65.210.17, 74.65.210.17', 'url': 'https://httpbin.org/get'}

with open("data2.json", "w") as write_file:
    json.dump(data, write_file)