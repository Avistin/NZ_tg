import requests
import fake_useragent
from bs4 import BeautifulSoup

logining_link = https://nz.ua/
datas = {
    'LoginForm[login]':'def'
    'LoginForm[password]':'def'
}
login = input('Введіть ваш логін ')
password = input('Введіть ваш пароль ')
datas['LoginForm[login]'] = login
datas['LoginForm[password]'] = password
url = 'https://nz.ua'
s = requests.Session()
logining = s.post(url, data = datas)
f = open('result.txt', 'w+')
f.write()
f.close()