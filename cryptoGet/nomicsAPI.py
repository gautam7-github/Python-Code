import json
import datetime
import requests
from argparse import ArgumentParser, SUPPRESS
import sys
import tabulate
from isvalidCurr import *
from isvalidCoin import *
'''
c180a29bade4d80315a19514d03c1eff
"https://api.nomics.com/v1/currencies/ticker?key=c180a29bade4d80315a19514d03c1eff&ids=BTC&interval=1d,30d&convert="
'''


def get_nomics_data(curr, coin, hold=1.00):
    API_KEY = "c180a29bade4d80315a19514d03c1eff"
    currency = curr.upper()
    coin = coin.upper()
    if not (isvalidCurr(currency=currency) and isvalidCoin(COIN=coin)):
        print("ERROR IN ARGS")
        exit()
    print("GETing Response from Nomics API")
    url = "https://api.nomics.com/v1/currencies/ticker?key="+API_KEY+"&ids=" + \
        coin + "&convert=" + currency
    response = requests.get(url=url)
    if response.status_code >= 200 and response.status_code < 300:
        response_JSON = json.loads(json.dumps(response.json(), indent=4))
        for i in response_JSON:
            # print(type(i['price']))
            print(
                tabulate.tabulate(
                    [
                        ["NAME", "SYMBOL", "TO CURRENCY"],
                        [i['name'], i['symbol'], currency]
                    ],
                    headers="firstrow",
                    tablefmt="psql"
                )
            )
            print(
                tabulate.tabulate
                (
                    [["TIME-STAMP"], [datetime.datetime.now()]],
                    headers="firstrow",
                    tablefmt="psql"
                )
            )
            print(
                tabulate.tabulate(
                    [
                        ["PRICE", "QUANTITY"],
                        [float(i['price']), "1"]
                    ],
                    headers="firstrow",
                    tablefmt="psql"
                )
            )
            if hold != 1.00:
                print(
                    tabulate.tabulate(
                        [
                            ["HOLD PRICE", "HOLD QNT"],
                            [float(i['price']) * hold, hold]
                        ],
                        headers="firstrow",
                        tablefmt="psql"
                    )
                )
        return url, response_JSON


'''
def isvalidCurr(currency='INR'):
    with open(f'supportedCurr.json', 'r') as JsFile:
        data = json.load(JsFile)
        # print(json.dumps(data, indent=4))
        res = json.loads(json.dumps(data, indent=4))
        for r in res:
            if r['currency'] == currency:
                print(f"{currency} is valid")
                return True
                break
        else:
            return False
'''

'''
def isvalidCoin(COIN="BTC"):
    with open("coins.json", "r") as Jfile:
        data = json.load(Jfile)
        coin = json.loads(json.dumps(data, indent=4))
        # print(coin)
        for c in coin:
            if c['symbol'] == COIN.lower():
                print(f"{COIN} is valid")
                return True
                break
        else:
            print(f"{COIN} is invalid")
            return False
'''


def main():
    parser = ArgumentParser(
        prog="cryptoGet.py",
        description="CRYPTO TRACKER",
        add_help=False)
    required = parser.add_argument_group("Required Arguments")
    optional = parser.add_argument_group("Optional Arguments")
    optional.add_argument(
        "-h",
        "-help",
        action="help",
        default=SUPPRESS,
        help="HELP"
    )
    required.add_argument(
        "-coin", help="Choose your coin", type=str, required=True)
    required.add_argument(
        "-currency", help="Currency Symbol", required=True)
    optional.add_argument(
        "-holding", help="HOLDINGS", required=False)
    # parses all the given args and convert them into a dictionary
    ARGS = vars(parser.parse_args())
    # print(f"{ARGS} are the given arguments")
    # print(ARGS['coin'])
    # print(ARGS.get('currency'))
    # if isvalidCurr(ARGS['coin']):
    url, res = get_nomics_data(
        ARGS['currency'], ARGS['coin'], float(ARGS['holding'])
    )


if __name__ == "__main__":
    main()
