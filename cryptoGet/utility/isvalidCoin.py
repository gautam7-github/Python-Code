import json


def isvalidCoin(COIN="BTC"):
    with open("utility/supportedCoins.json", "r") as Jfile:
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
