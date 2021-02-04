
def args_help():
    help_string = """
                cryptoGet - Your CryptoTracker

        USAGE ->
               cryptoGet.py -COIN CURRENCY -HOLD [HOLD]

            ARGUMENTS:
                -COIN    : REQUIRED
                CURRENCY : REQUIRED
                -HOLD     : OPTIONAL

        EXAMPLES ->
               EXAMPLE : cryptoGet.py -btc inr -hold 0.06
               EXAMPLE : cryptoGet.py -doge usd -hold 400

        POWERED BY ->
            CoinMarketCap API
            Nomics API
            CoinGecko API
    """
    print(help_string)


if __name__ == "__main__":
    args_help()
