import requests
from bs4 import BeautifulSoup
import json

def getJsonFromURL(url):
    s = requests.Session()
    print(f"Requesting URL : {url}")
    resp = s.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')
    data = json.loads(str(soup))
    return data
url = 'http://www.psudataeng.com:8000/getBreadCrumbData'
data = getJsonFromURL(url)
hundreddata = []
for i in range(1000):
    hundreddata.append(data[i])
# hundredjsondata = json.dumps(hundreddata)
# print(type(hundredjsondata))
with open('file.json', 'w') as jsonfile:
    json.dump(hundreddata, jsonfile)
