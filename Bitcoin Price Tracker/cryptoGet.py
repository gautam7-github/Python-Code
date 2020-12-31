''' 
    0             1   2   3   4
    btcprice.py -btc INR -w res.json
    btcprice.py -btc USD
'''

import datetime
import requests
import json
import time
import matplotlib.pyplot as plt
import sys
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def get_BTC(args_list):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/' + \
        args_list[2].upper() + '.json'
    response = requests.get(url)
    if response.status_code < 300 and response.status_code >= 200:
        # print(response.status_code)
        res = json.loads(json.dumps(response.json(), indent=4))
        data = res['bpi'][args_list[2]]['rate']
        return data, res
    else:
        print(response.status_code)
        return multiple_BTC(args_list), 1


def multiple_BTC(args_list):
    return cg.get_price(ids='bitcoin', vs_currencies=args_list[2].lower())['bitcoin'][args_list[2].lower()]


def main_BTC(args_list):

    print("BITCOIN PRICE : "+args_list[2]+" -> ", end='')
    #cg.get_price(ids='litecoin', vs_currencies='inr')
    # for debugging
    # print(args_list)
    if not isvalidCurr(args_list[2]):
        print("NOT A VALID CURRENCY SYMBOL....")
        exit()
    data, res = get_BTC(args_list)
    print(data)
    if '-plt' in sys.argv:
        plt.plot(data, datetime.datetime.now())
        plt.show()
    if len(args_list) > 3:
        if args_list[3] == "-w":
            with open(args_list[4], 'w') as file:
                json.dump(res, file, indent=4)


def isvalidCurr(currency='INR'):
    with open(f'files-json\supportedCurr.json', 'r') as JsFile:
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
            i = 1
            while i != 3:
                main_BTC(sys.argv)
                # time.sleep(60)
                i += 1
        if sys.argv[1] == "-ltc":
            print(cg.get_price(ids='litecoin', vs_currencies=sys.argv[2].lower())[
                'litecoin'][sys.argv[2].lower()])
    else:
        print("NO ARGUMENTS PASSED....")
