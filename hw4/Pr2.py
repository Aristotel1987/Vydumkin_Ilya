import requests
import json
nick = input('Введите логин пользователя github, информация о котором ас интересует')
resp =  requests.get('https://api.github.com/users/'+nick)
answ = resp.text
data = json.loads(answ)
print(f'Логин пользователя: {data['login']}\nИмя пользователя: {data['name']}\nКоличество публичных репозиториев: {data['public_repos']}')









