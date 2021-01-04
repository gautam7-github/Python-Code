'''
    0             1   2   3   4
    btcprice.py -btc INR -w res.json
    btcprice.py -btc USD
'''
# TODO Create BTC Class
import datetime
import requests
import json
import time
import matplotlib.pyplot as plt
import sys
from pycoingecko import CoinGeckoAPI


def get_BTC(args_list):
    code, data, res = get_coindesk_BTC(args_list)
    if code:
        return data, res
    else:
        return get_coinGecko(args_list, 'bitcoin')


def get_coindesk_BTC(args_list):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/' + \
        args_list[2].upper() + '.json'
    response = requests.get(url)
    if response.status_code < 300 and response.status_code > 200:
        # print(response.status_code)
        res = json.loads(json.dumps(response.json(), indent=4))
        return True, res['bpi'][args_list[2]]['rate_float'], res
    else:
        return False, None, None


def get_coinGecko(args_list, coin: str):
    cg = CoinGeckoAPI()
    res = cg.get_price(ids=coin, vs_currencies=args_list[2].lower())
    data = res[coin][args_list[2].lower()]
    return data, res


def main_BTC(args_list):
    coins = {}
    # checking coin symbol and id
    with open("coins.json", "r") as Jfile:
        data = json.load(Jfile)
        coin = json.loads(json.dumps(data, indent=4))
        # print(coin)
        for c in coin:
            if c['symbol'] == args_list[1][1:]:
                coins = c
                break
    if not isvalidCurr(args_list[2]):
        print("NOT A VALID CURRENCY SYMBOL....")
        exit()

    print(coins['id'].upper() + " PRICE : "+args_list[2]+" -> ", end='')
    # for debugging
    # print(args_list)
    # print(coins[sys.argv[1]])
    data, res = get_BTC(args_list)
    print(data)
    # print(res)
    if '-plt' in sys.argv:
        plt.plot(data, datetime.datetime.now(), 'ro')
        plt.show()
    if len(args_list) > 3:
        if args_list[3] == "-w":
            with open(args_list[4], 'w') as file:
                json.dump(res, file, indent=4)


def isvalidCurr(currency='INR'):
    with open(f'supportedCurr.json', 'r') as JsFile:
        data = json.load(JsFile)
        # print(json.dumps(data, indent=4))
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
        main_BTC(sys.argv)
    else:
        print("REQUIRED ARGUMENTS -NOT- PASSED....")
