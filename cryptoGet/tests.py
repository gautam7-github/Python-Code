import json
import datetime
import requests
from argparse import ArgumentParser, SUPPRESS
import sys
'''
c180a29bade4d80315a19514d03c1eff
"https://api.nomics.com/v1/currencies/ticker?key=c180a29bade4d80315a19514d03c1eff&ids=BTC&interval=1d,30d&convert="
'''


def get_nomics(curr, coin):
    currency = curr.upper()
    coin = coin.upper()
    url = "https://api.nomics.com/v1/currencies/ticker?key=c180a29bade4d80315a19514d03c1eff&ids=" + \
        coin + "&interval=1d,30d&convert="
    url = url + currency
    print(url)
    response = requests.get(url=url)
    # print(response.json())
    response_JSON = json.loads(json.dumps(response.json(), indent=4))
    for i in response_JSON:
        # print(type(i['price']))
        print(f"{i['symbol']} : {i['name']} : {currency}")
        print(f"{float(i['price'])} : PRICE AT {datetime.datetime.now()}")


def showhelp():
    print("\t\t--HELP--")


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="cryptoGet.py",
        description="CRYPTO TRACKER",
        add_help=False)
    required = parser.add_argument_group("Required Arguments")
    optional = parser.add_argument_group("Optional Arguments")
    optional.add_argument("-h", "-help",
                          action="help",
                          default=SUPPRESS,
                          help=showhelp())
    required.add_argument(
        "-coin", help="Choose your coin", type=str, required=True)
    required.add_argument(
        "-currency", help="Currency Symbol", required=True)
    A = parser.parse_args()
    print(A)
    # print(A.btc)
    if A.coin:
        # print(A.currency)
        get_nomics(A.currency, A.coin)
    '''if len(sys.argv) > 2:
        get_nomics(sys.argv[2])
'''
