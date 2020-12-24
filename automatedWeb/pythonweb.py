import requests
import bs4
import html

res = bs4.BeautifulSoup("www.google.com", 'html.parser')
print(res.prettify())
