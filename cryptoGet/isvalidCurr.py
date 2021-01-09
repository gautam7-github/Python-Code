import json


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
