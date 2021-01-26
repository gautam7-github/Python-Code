import json


def get_coin_name(coin_OG="BTC"):
    with open("utility/supportedCoins.json", "r") as Jfile:
        data = json.load(Jfile)
        coin = json.loads(json.dumps(data, indent=4))
        for cursor in coin:
            if cursor['symbol'] == coin_OG.lower():
                return cursor['name']
        return None
