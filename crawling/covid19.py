# Source: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
import os
import requests


_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
confirmed_url = _URL+"time_series_covid19_confirmed_global.csv"
deaths_url = _URL+"time_series_covid19_deaths_global.csv"
recovered_url = _URL+"time_series_covid19_recovered_global.csv"
urls = [confirmed_url, deaths_url, recovered_url]

def _download(csv_url):
    name = csv_url.split('/')[-1]
    path = os.path.join('.','data',name)
    req = requests.get(csv_url)
    with open(path, 'wb') as csv_file:
        csv_file.write(req.content)
    
    del name, path, req

def get_datasets():
    for url in urls:
        _download(url)

if __name__=="__main__":
    get_datasets()