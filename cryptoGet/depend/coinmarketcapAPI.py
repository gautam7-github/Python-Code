import requests
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates, CurrencyCodes


def get_coinmarketcap_data(curr='USD', coin='bitcoin', hold=1.00):
    conv_curr = CurrencyRates()
    codes = CurrencyCodes()
    url = 'https://coinmarketcap.com/currencies/' + coin + '/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    coin_val = soup.find(
        "div",
        {
            "class": "priceValue___11gHJ"
        }
    )
    for price in coin_val:
        local_curr = conv_curr.convert(
            'USD', 'INR', float((price[1:]).replace(",", "")))
        print(f"USD : {price}")
        local_symbol = codes.get_symbol('INR')
        print(f"INR : {local_symbol}{round(local_curr,2)}")


if __name__ == "__main__":
    print("ACCESS TO THIS FILE IS RESTRICTED...")
    get_coinmarketcap_data("INR", "BTC", 2)
