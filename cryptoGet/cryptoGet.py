'''
    0             1   2    3
    btcprice.py -btc  INR  4
    btcprice.py -btc  USD  4
    btcprice.py -doge INR  286
'''
# built in modules
import datetime
import json
import logging
import sys
import time

# external modules
import matplotlib.pyplot as plt
import requests
from pycoingecko import CoinGeckoAPI

# dependencies
from depend.nomicsAPI import *
from depend.coinmarketcapAPI import *
from utility.getCoinName import *
from utility.help import args_help


def get_coingecko(args_list):
    cg = CoinGeckoAPI()
    coin = coins[args_list[1][1:]]
    res = cg.get_price(
        ids=coin,
        vs_currencies=args_list[2].lower()
    )
    data = res[coin][args_list[2].lower()]
    print(data)
    print(" -> ")
    print(coin)


def main(args_list: list):
    '''
    Give me a list of arguments and I'll return something
    '''
    error_codes = {
        402: "__INVALID ARGUMENTS__",
        404: "__API ERROR__"
    }
    CURRENCY = args_list[2]
    COIN_SYMBOL = args_list[1][1:]
    COIN_NAME = get_coin_name(COIN_SYMBOL)
    Hold = 1.00
    if len(args_list) >= 4 and "-hold" in args_list:
        Hold = float(args_list[-1])
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


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        print(sys.argv)
        main(sys.argv)
    elif "-help" in sys.argv:
        args_help()
