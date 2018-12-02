import random
url = 'http://bolshe.com.ua/form/addAds'
import string
N = 88

import urllib.request as urllib2

def randomInt(c=1):
    return ''.join(random.SystemRandom().choice(string.digits ) for _ in range(c))
def randomChar(c=1):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase ) for _ in range(c))

def randomData():
    global d
    d['parent_id'] = randomInt(2)
    d['cost'] = randomInt(int(randomInt(1)))
    d['text'] += randomChar(25)
    d['PHONES[]'] +=  randomInt(2)


d = {
'parent_id': randomInt(2),
#randomInt(3)
'city_id': '207',
'name': 'УДАЛИТЕ МОЙ НОМЕР ТЕЛЕФОНА Я НЕ ПРОДАЮ УДАРНУЮ УСТАНОВКУ ALESIS DM7X ЗА 1500, Я ПРОДАЮ ЕЁ ЗА 15000 и только на olx.ua',
'city': 'Киевская область, Киев',
'cost': randomInt(int(randomInt(1))),
'currency': '0',
'brand_id': 'fender-12',
'text': """УДАЛИТЕ МОЙ НОМЕР ТЕЛЕФОНА Я НЕ ПРОДАЮ УДАРНУЮ УСТАНОВКУ ALESIS DM7X ЗА 1500, Я ПРОДАЮ ЕЁ ЗА 15000 и только на olx.ua'
        'НЕ ЗВОНИТЕ МНЕ НИКОГДА ЕСЛИ НЕ СОБИРАЕТЕСЬ ПОКУПАТЬ УСТАНОВКУ ЗА 15000 ГРИВЕН (НЕ КОПЕЕК) ИЛИ ДОРОЖЕ'
        'ПОЛЬЗУЕТЕСЬ Б* * Л * * Я * * Я * * Т * * Б * * ПРОВЕРЕННЫМИ САЙТАМИ А НА ЭТО ГОВНО БОЛЬШЕ НЕ ЗАХОДИТЕ НИКОГДА'
        'А ЕЩЁ ОНО ВЫДАЛО МНЕ ФРАГМЕНТ ПРОГРАММНОГО КОДА ТАК ЧТО Я ПЕРЕХЪРАЧУ ВАЩ САЙТ К ХУЯМ ЕСЛИ НЕ УДАЛИТЕ'
        'МНЕ СПАТЬ СПОКОЙНО НЕ ДАЮТ""",
'author_name': 'Этот-сайт-копирует-объявления-с-олх',
'author_email': 'qwerty@qweqe.com',
#'PHONES[]':  '38 (066) ' + randomChar(3) + '-' + randomInt(2) + '-' + randomInt(2),

'PHONES[]':  '38 (066) ' + 'XYI-TE-',
'author_skype': 'Этот-сайт-копирует-объявления',
'VIDEO[]': '',
'free': '1',
'top': '1',
'top_period_days': '1',
'token': 'YWQ1NTVhOGY1OTBiZDEyZmRlMzhiNjJmMjFmMjRjYTA1YTExMGUxZjU4OGJjYzI2YTkzMDYxZDFjMDc1ODYyOA',
#'token': 'YWQ1NTVhOGY1OTBiZDEyZmRlMzhiNjJmMjFmMjRjYTA1YTExMGUxZjU4OGJjYzI2YTkzMDYxZDFjMDc1ODYyOA==',
'user_agreement': 'on'
}

headers = {'Content-type': 'multipart/form-data',
           'Referer': 'http://bolshe.com.ua/advert/create'
}
c = {
'PHPSESSID': 'o5rcenibmsluajthkif7a4ncn2',
'currency':'f86cf62636de71253f1072dd9076f131804a231f%7E1',
'_ga':'GA1.3.2072429213.1539447742',
'_gid':'GA1.3.1500865034.1539447742',
'_a_d3t6sf':'dupxXS414sXSBzCqgKADophT',
'viewed':'e2481645fd55ff08a3c6a66762f6e68345cb3931%7EWyI3NTQwNyJd',
'cart': 'd5681f5d5f650fa1b55804784eb04a8b6cb12f1d%7E500616bdca182bdfa1a0e5c4c467570d2344e11f',
'_hjIncludedInSample': '1',
'user': '9b25c5fa1443f39d01be1e9730c532d906d935f2%7EeyJyZW1lbWJlciI6MCwiZXhpdCI6MCwiaWQiOiIyMzE0NCJ9',
'_dc_gtm_UA-65864022-1': '1',
'_gat_UA-65864022-1': '1'
}

#d['PHONES[]'] += ''.join(random.SystemRandom().choice(string.digits) for _ in range(3))
#d['PHONES[]'] += '-'
#d['PHONES[]'] += ''.join(random.SystemRandom().choice(string.digits) for _ in range(2))
#d['PHONES[]'] += '-'
#d['PHONES[]'] += ''.join(random.SystemRandom().choice(string.digits) for _ in range(2))
print(d['PHONES[]'])
#d['token'] += ''.join(random.SystemRandom().choice(string.ascii_uppercase ) for _ in range(2)) + "=="
d['token'] += "=="
print(d['token'])
import requests
import json
succ = 0
fail = 0
for i in range(0,1):
    r = requests.post(url, data=d)
    file  = open('1.html', 'w')
    file.write(str(r.content))
    file.close()
    content = r.content
    data = []
    randomData()
    try:
        print("number",d["PHONES[]"])
        data = json.loads(content)
        succ+=1
    except Exception as e:
        print(e)
        print(content)
        fail +=1

print("result: ", succ,fail,succ+fail)