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
from utility.getCoinName import *


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
    CURRENCY = args_list[2]
    COIN_SYMBOL = args_list[1][1:]
    COIN_NAME = get_coin_name(COIN_SYMBOL)
    Hold = 1.00
    if len(args_list) >= 4:
        Hold = float(args_list[3])
        code, response_nomics = get_nomics_data(
            args_list[2], args_list[1][1:], Hold)
    else:
        code, response_nomics = get_nomics_data(
            args_list[2], args_list[1][1:], Hold)
    if code in error_codes or response_nomics is None:
        if code == 404:
            get_coinmarketcap_data(CURRENCY, COIN_NAME, Hold)
        else:
            print(error_codes[code])
            args_help()
    else:
        data = response_nomics[0]['price']
        data_meta = response_nomics[0]['name']


def args_help():
    help_string = """
                cryptoGet - Your CryptoTracker

        USAGE ->
               cryptoGet.py -COIN CURRENCY [HOLD]

            ARGUMENTS:
                -COIN    : REQUIRED
                CURRENCY : REQUIRED
                HOLD     : OPTIONAL

        EXAMPLES ->
               EXAMPLE : cryptoGet.py -btc inr 0.06
               EXAMPLE : cryptoGet.py -doge usd 400

        POWERED BY ->
            CoinMarketCap API
            Nomics API
            CoinDesk API
            CoinGecko API
    """
    print(help_string)


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        main(sys.argv)
    elif "-h" in sys.argv or "-help" in sys.argv:
        args_help()
