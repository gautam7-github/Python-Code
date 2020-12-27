'''
    btcprice.py -btc INR
    btcprice.py -btc USD
'''


import requests
import json
import sys


url = 'https://api.coindesk.com/v1/bpi/currentprice/' + sys.argv[2] + '.json'
response = requests.get(url)

res = json.loads(json.dumps(response.json(), indent=4))
print(res['bpi'][sys.argv[2]]['rate'])
with open('res.json', 'w') as file:
    json.dump(res, file, indent=4)
