import json
import datetime
import requests
'''
c180a29bade4d80315a19514d03c1eff
'''
url = "https://api.nomics.com/v1/currencies/ticker?key=c180a29bade4d80315a19514d03c1eff&ids=BTC&interval=1d,30d&convert=INR&per-page=100&page=1"
response = requests.get(url=url)
# print(response.json())
o = json.loads(json.dumps(response.json(), indent=4))
for i in o:
    print(f"{i['symbol']} {i['name']}")
    print(f"{i['price']} : PRICE AT {datetime.datetime.now()}")
