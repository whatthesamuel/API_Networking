import requests
import json
import time

url = 'http://localhost:5000/'

def make_request(endpoint, method, data):
    headers = {'Content-type': 'application/json'}
    if method == 'POST':
        response = requests.post(url + endpoint, data=json.dumps(data), headers=headers)
    elif method == 'GET':
        response = requests.get(url + endpoint, data=json.dumps(data), headers=headers)
    else:
        print("Invalid method")
        return
    return response.json()


def Login():
    data = {'name': 'Lorem'}
    print(make_request('AddPlayer', 'POST', data))

def GetPlayerData():
    data = {'name': 'Lorem'}
    print(make_request('GetPlayer', 'GET', data))

def DamagePlayer():
    data = {'name': 'Lorem', "hp": 10}
    make_request('UpdatePlayer', 'POST', data)

Login()
time.sleep(1) # delay for internet latency, logic processing...
GetPlayerData()
time.sleep(1) # delay for internet latency, logic processing...
DamagePlayer()