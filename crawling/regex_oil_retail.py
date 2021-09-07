import re

import requests
from bs4 import BeautifulSoup

URL = "http://www.shell.com.sg/motorists/shell-fuels/shell-station-price-board.html"

def get_oil_retail():
    extracted_data = {}
    price_data = []
    product_data = []
    
    html_contents = requests.get(URL).text
    soup = BeautifulSoup(html_contents, "lxml")
    list_text = soup.find_all("td")
    seq = [item.get_text() for item in list_text]
    _price_data = [float(''.join(re.findall(r'[\d.]+', item))) for item in seq[1::3]]

    len_data = len(_price_data)
    product_data += [item.rstrip() for item in seq[::3]]
    price_data += _price_data
    extracted_data['product'] = product_data
    extracted_data['price'] = price_data
    
    print(extracted_data)


if __name__=="__main__":
    get_oil_retail()