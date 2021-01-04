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
    print("GETing Response from Nomics API")
    currency = curr.upper()
    coin = coin.upper()
    url = "https://api.nomics.com/v1/currencies/ticker?key=c180a29bade4d80315a19514d03c1eff&ids=" + \
        coin + "&convert=" + currency
    # print(url)
    response = requests.get(url=url)
    # print(response.json())
    if response.status_code >= 200 and response.status_code < 300:
        response_JSON = json.loads(json.dumps(response.json(), indent=4))
        for i in response_JSON:
            # print(type(i['price']))
            print(f"{i['symbol']} : {i['name']} : {currency}")
            print(f"PRICE AT {datetime.datetime.now()} : {float(i['price'])}")


def showhelp():
    print("\t\t--HELP--")


if __name__ == "__main__":
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
        help=showhelp()
    )
    required.add_argument(
        "-coin", help="Choose your coin", type=str, required=True)
    required.add_argument(
        "-currency", help="Currency Symbol", required=True)
    optional.add_argument(
        "-url", help="Prints the request URL")
    A = parser.parse_args()
    # print(A)
    print(A)
    print(A.coin)
    print(A.currency)
    if A.coin:
        get_nomics(A.currency, A.coin)
