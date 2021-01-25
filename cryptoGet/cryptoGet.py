'''
    0             1   2    3
    btcprice.py -btc  INR  4
    btcprice.py -btc  USD  4
    btcprice.py -doge INR  286
'''
import datetime
import json
import logging
import sys
import time

import matplotlib.pyplot as plt
import requests
from pycoingecko import CoinGeckoAPI

from depend.nomicsAPI import *
from depend.coinmarketcapAPI import *


def get_coindesk_btc(args_list):
    """ CoinDesk API """
    url = 'https://api.coindesk.com/v1/bpi/currentprice/' + \
        args_list[2].upper() + '.json'
    response = requests.get(url)
    if response.status_code < 300 and response.status_code > 200:
        # print(response.status_code)
        res = json.loads(json.dumps(response.json(), indent=4))
        return True, res['bpi'][args_list[2]]['rate_float'], res
    return False, None, None


def get_coingecko(args_list):
    cg = CoinGeckoAPI()
    coins = {
        'btc': 'bitcoin',
        'ltc': 'litecoin',
        'doge': 'dogecoin',
        'xlm': 'stellar'
    }
    coin = coins[args_list[1][1:]]
    res = cg.get_price(
        ids=coin,
        vs_currencies=args_list[2].lower()
    )
    data = res[coin][args_list[2].lower()]
    print(data)
    print(" -> ")
    print(coin)


def main(args_list):
    error_codes = {
        402: "__INVALID ARGUMENTS__",
        404: "__API ERROR__"
    }
    code, response_nomics = get_nomics_data(
        args_list[2], args_list[1][1:], float(args_list[3]))
    if code in error_codes and response_nomics is None:
        if code == 404:
            get_coingecko(args_list)
        else:
            print(error_codes[code])
    data = response_nomics[0]['price']
    data_meta = response_nomics[0]['name']
    # print(data+" " + data_meta)
    """if '-plt' in sys.argv:
        plt.plot(data, datetime.datetime.now(), 'ro')
        plt.title(data_meta)
        plt.show()"""


def args_help():
    help_string = """
    REQUIRED ARGUMENTS -NOT- PASSED....

        USAGE ->
               cryptoGet.py -COIN CURRENCY [HOLD]
            ARGUMENTS:
               -COIN : REQUIRED
                CURRENCY : REQUIRED
                HOLD : OPTIONAL

        EXAMPLES ->
               EXAMPLE : cryptoGet.py -btc inr 0.06
               EXAMPLE : cryptoGet.py -doge usd 400
    """
    print(help_string)


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1][0] == "-":
        main(sys.argv)
    else:
        args_help()
