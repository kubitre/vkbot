import vk
import time
import requests as req
from lxml import html

app_id, login, password = 'app_id', 'login', 'password'
session = vk.AuthSession(app_id, login, password, scope='messages')
vk_api = vk.API(session, v='5.62')

while True:
    massages=vk_api.messages.getDialogs(count=20, unread=1)
    print(massages)
   
    if massages['count']==1:
        print('Новое письмо', massages)
        id = massages['items'][0]['message']['user_id']
        body=massages['items'][0]['message']['body']
        print(id, body)

        if body.lower()=='спокойной ночи':
            vk_api.messages.send(user_id=id, message="Спококйной ночи!))Мурк")
            print()
        
    elif massages['count']==0:
        print('Новых писем нет')
    time.sleep(1)