'''
    0             1   2   3   4
    btcprice.py -btc INR -w res.json
    btcprice.py -btc USD
'''
import datetime
import json
import sys
import time

import matplotlib.pyplot as plt
import requests
from pycoingecko import CoinGeckoAPI

from depend.nomicsAPI import *


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
    # for debugging
    # print(args_list)
    # print(coins[sys.argv[1]])
    # print(res)
    if len(args_list) > 3:
        url, response_nomics = get_nomics_data(
            args_list[2], args_list[1][1:], float(args_list[3]))
        data = response_nomics[0]['price']
        data_meta = response_nomics[0]['name']
    if '-plt' in sys.argv:
        plt.plot(data, datetime.datetime.now(), 'ro')
        plt.title(data_meta)
        plt.show()


if __name__ == "__main__":
    if len(sys.argv) > 2:
        main_BTC(sys.argv)
    else:
        print("REQUIRED ARGUMENTS -NOT- PASSED....")
        print("USAGE ->")
        print("cryptoGet.py -COIN CURRENCY [HOLD]")
        print("EXAMPLE : cryptoGet.py -btc inr 0.06")
        print("EXAMPLE : cryptoGet.py -doge usd 400")