''' 
    0             1   2   3   4
    btcprice.py -btc INR -w res.json
    btcprice.py -btc USD
'''


import requests
import json
import sys


def main(args_list):
    if not isvalidCurr(args_list[2]):
        print("NOT A VALID CURRENCY SYMBOL....")
        exit()
    url = 'https://api.coindesk.com/v1/bpi/currentprice/' + \
        args_list[2] + '.json'
    response = requests.get(url)
    res = json.loads(json.dumps(response.json(), indent=4))
    print("BITCOIN PRICE : "+args_list[2]+" -> ", end='')
    print(res['bpi'][args_list[2]]['rate'])
    if args_list[3] == "-w":
        with open(args_list[4], 'w') as file:
            json.dump(res, file, indent=4)


def isvalidCurr(currency='INR'):
    with open('supportedCurr.json', 'r') as JsFile:
        data = json.load(JsFile)
        #print(json.dumps(data, indent=4))
        res = json.loads(json.dumps(data, indent=4))
        for r in res:
            if r['currency'] == currency:
                return True
    JsFile.close()


if __name__ == "__main__":
    if len(sys.argv) > 2:
        if sys.argv[1] == "-btc":
            main(sys.argv)
            isvalidCurr()
    else:
        print("NO ARGUMENTS PASSED....")
