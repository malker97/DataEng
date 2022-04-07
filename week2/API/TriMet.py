# https://developer.trimet.org/ws/V1/arrivals?locIDs=6849,6850&appID=2B4A2694B832D6CDB45908BDB
# To get a list of every stop considered a time point in direction 1 of route number 70 in json
# https://developer.trimet.org/ws/V1/routeConfig/route/70/dir/1/tp/true/json/true/appid/2B4A2694B832D6CDB45908BDB
# To get a list of every stop considered a time point in direction 1 of route number 70
# https://developer.trimet.org/ws/V1/routeConfig/route/70/dir/1/tp/true/json=true/appid/2B4A2694B832D6CDB45908BDB
# PSU Stattion Name: PSU Urban Center/SW 6th & Montgomery
# PSU Stattion ID: 7774,607,10293,10491,13305,7618,7773,616
# PSU Stattion Name: PSU South/SW 6th & College
# PSU Stattion ID: 10293
# arrive at 7774 data :https://developer.trimet.org/ws/v2/arrivals/locIDs/7774/appid/2B4A2694B832D6CDB45908BDB
# Question 1:
#   What buses are arriving at the PSU campus soon?
# https://developer.trimet.org/ws/v2/arrivals/locIDs/7774/appid/2B4A2694B832D6CDB45908BDB
from operator import ge
import requests
from bs4 import BeautifulSoup
import json

appid = '2B4A2694B832D6CDB45908BDB'
locIDs = '607,13305,10491,5009,12763,7773,'

s = requests.Session()
url = f"https://developer.trimet.org/ws/v2/arrivals/minutes/10/locIDs/{locIDs}/7774/appid/{appid}"
# print(url)
print(f"Requesting URL : {url}")
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
data = json.loads(str(soup))
# print(len(data['resultSet']['arrival']))
buses = set()
for bus in data['resultSet']['arrival']:
    # The number of the direction, either 1 for inbound or 0 for outbound.
    if bus['dir'] == 1:
        buses.add(bus['vehicleID'])
        # print(bus['vehicleID'])
    # print(bus['vehicleID'])
# sorted(buses)
print('What buses are arriving at the PSU campus soon?')
print(f'{buses} will arrive PSU in 10 mins')
print(f'Number of Arrival: {len(buses)}')
# route 12 blockID	:	1202
# https://developer.trimet.org/ws/v2/vehicles
print('Do you ride a bus? When is its next arrival?')
routes = 12
blockID = 1202
print(f"Yes, I take buses route {routes} at block {blockID}")
url = f'https://developer.trimet.org/ws/v2/vehicles/routes/{routes}/blocks/{blockID}/appid/{appid}'
resp = s.get(url)
print(f"Requesting URL : {url}")
soup = BeautifulSoup(resp.text,'html.parser')
data = json.loads(str(soup))
print("There is ",len(data['resultSet']['vehicle']), 'Buses will arrive my block')

# https://developer.trimet.org/ws/V1/routeConfig
print("Which route has the most stops?")
url = f'https://developer.trimet.org/ws/V1/routeConfig/json/true/stops/true/appid/{appid}'
print(url)
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
data = json.loads(str(soup))
print(len(data['resultSet']['route']))
routesNum = set()
for route in data['resultSet']['route']:
    routesNum.add(route['id'])
# print(routesNum)
maxStop = 0
maxStopRoute = 0
for i in routesNum:
    url = f'https://developer.trimet.org/ws/V1/routeConfig/route/{i}/json/true/dir/true/stops/true/appid/{appid}'
    print(f"Requesting URL : {url}")
    resp = s.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')
    data = json.loads(str(soup))
    # print(len(data['resultSet']['route'][0]['dir'][1]))
    dir1 = data['resultSet']['route'][0]['dir'][0]['stop']
    dir2 = data['resultSet']['route'][0]['dir'][0]['stop']
    stops = len(dir1) + len(dir2)
    if(stops > maxStop):
        # print(stops)
        maxStop = stops
        maxStopRoute = i
print("The Route ", maxStopRoute ," has the most stops")  
