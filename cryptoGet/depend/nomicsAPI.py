import json
import datetime
import requests
from argparse import ArgumentParser, SUPPRESS
import sys
import tabulate
from depend.secrets import nomicsAPIKEY
from utility.isvalidCurr import *
from utility.isvalidCoin import *


'''
"https://api.nomics.com/v1/currencies/ticker?key=API_KEY&ids=BTC&interval=1d,30d&convert="
'''


def get_nomics_data(curr='usd', coin='btc', hold=1.00):
    API_KEY = nomicsAPIKEY
    currency = curr.upper()
    coin = coin.upper()
    if not (isvalidCurr(currency=currency) and isvalidCoin(COIN=coin)):
        return 402, None
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
                    tablefmt="psql",
                    floatfmt="20.3f"
                )
            )
            if hold != 1.00:
                total = float(i['price']) * hold
                print(
                    tabulate.tabulate(
                        [
                            ["HOLD PRICE", "HOLD QNT"],
                            [total, hold]
                        ],
                        headers="firstrow",
                        tablefmt="psql",
                        floatfmt="20.3f"
                    )
                )
        return 200, response_JSON
    return 404, None


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
    url, res = get_nomics_data(
        ARGS['currency'], ARGS['coin'], float(ARGS['holding'])
    )


if __name__ == "__main__":
    main()
