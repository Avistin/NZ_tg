import requests
import fake_useragent
from bs4 import BeautifulSoup

session = requests.Session()

link = 'https://nz.ua'

user = fake_useragent.UserAgent().random

header = {
    'user-agent': user
}

data = {
    'LoginForm[login]': 'ivanovich_bogdan',
    'LoginForm[password]': 'retro005'
}
responce = session.post(link, data=data, headers=header).text
print(responce)