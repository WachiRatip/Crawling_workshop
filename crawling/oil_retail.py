import os

import requests
from bs4 import BeautifulSoup

URL = "https://www.caltex.com/my/motorists/products-and-services/fuel-prices.html"

def get_oil_retail():
    html_contents = requests.get(URL).text
    soup = BeautifulSoup(html_contents, "lxml")
    list_text = soup.find_all("div", {"class": "price-item"})
    seq = [item.get_text().replace("\n", "").split("RM ") for item in list_text]
    print(seq)

if __name__=="__main__":
    get_oil_retail()