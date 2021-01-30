import json
import os
import sys


def isvalidCurr(currency='INR'):
    currency = currency.upper()
    with open(f'utility/supportedCurr.json', 'r') as JsFile:
        data = json.load(JsFile)
        res = json.loads(json.dumps(data, indent=4))
        for r in res:
            if r['currency'] == currency:
                return True
        return False


if __name__ == "__main__":
    print("DEBUG --- ")
    print(sys.argv)
    print(isvalidCurr(sys.argv[1]))
