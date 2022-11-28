import requests

url = 'https://nz.ua'
s = requests.Session()

user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
              'Gecko/20100101 Firefox/50.0')

data = {
    'login':'login',
    'password':'12345'
}

auth = requests.post(url, data = data, headers={'User-Agent':user_agent}).text
print(auth)