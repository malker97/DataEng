from operator import ge
from xml.etree.ElementTree import tostring
import requests
from bs4 import BeautifulSoup
import json

# my api key d85bbe49c797aac2dedddf5e0ed09b20
aPIkey = 'd85bbe49c797aac2dedddf5e0ed09b20'
cityName = 'Portland'
s = requests.Session()

url = f'https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={aPIkey}'
print("From the API:", url)
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
data = json.loads(str(soup))
print("Current Weather in Portland is :",data['weather'][0]['main'])
url = 'https://wttr.in/Portland?format=3'
print("From the API:", url)
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
print(str(soup))
antarcticaCityID = 6255152
SaharaCityID = 2386012
# ●	Is there greater humidity currently in Antarctica or in the Sahara?
# https://api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key}

def getHumidity(cityID):
    url = f'https://api.openweathermap.org/data/2.5/weather?id={cityID}&appid={aPIkey}'
    resp = s.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')
    data = json.loads(str(soup))
    print(f"{cityID}'s humidity is ",data['main']['humidity'])
    return data['main']['humidity']
antarcticaCityHumidity = getHumidity(antarcticaCityID)
SaharaCityHumidity = getHumidity(SaharaCityID)
print("antarcticaCityHumidity>SaharaCityHumidity") if antarcticaCityHumidity>SaharaCityHumidity else ( print("antarcticaCityHumidity<SaharaCityHumidity") if antarcticaCityHumidity<SaharaCityHumidity else print("antarcticaCityHumidity=SaharaCityHumidity") )

