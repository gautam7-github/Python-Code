''' 
    0             1   2   3   4
    btcprice.py -btc INR -w res.json
    btcprice.py -btc USD
'''

import datetime
import requests
import json
import matplotlib.pyplot as plt
import sys
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def main_BTC(args_list):

    cg.get_price(ids='litecoin', vs_currencies='inr')
    # for debugging
    # print(args_list)
    if not isvalidCurr(args_list[2]):
        print("NOT A VALID CURRENCY SYMBOL....")
        exit()
    url = 'https://api.coindesk.com/v1/bpi/currentprice/' + \
        args_list[2].upper() + '.json'
    response = requests.get(url)
    res = json.loads(json.dumps(response.json(), indent=4))
    print("BITCOIN PRICE : "+args_list[2]+" -> ", end='')
    data = res['bpi'][args_list[2]]['rate']
    if '-plt' in sys.argv:
        plt.plot(data, datetime.datetime.now())
        plt.show()
    print(data)
    if len(args_list) > 3:
        if args_list[3] == "-w":
            with open(args_list[4], 'w') as file:
                json.dump(res, file, indent=4)


def isvalidCurr(currency='INR'):
    with open('supportedCurr.json', 'r') as JsFile:
        data = json.load(JsFile)
        #print(json.dumps(data, indent=4))
        res = json.loads(json.dumps(data, indent=4))
        for r in res:
            if r['currency'] == currency:
                return True
                break
        else:
            return False
    JsFile.close()


if __name__ == "__main__":
    if len(sys.argv) > 2:
        if sys.argv[1] == "-btc":
            for _ in range(4):
                main_BTC(sys.argv)
        if sys.argv[1] == "-ltc":
            print(cg.get_price(ids='litecoin', vs_currencies=sys.argv[2].lower())[
                'litecoin'][sys.argv[2].lower()])
    else:
        print("NO ARGUMENTS PASSED....")
