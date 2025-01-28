import requests
import json
import time
def connect_to_server(url, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers,timeout=1)
    if response.status_code == 200:
        return response.text
    else:
        print("Error connecting to server:", response.status_code)
        return None
def search(string):
    return connect_to_server("https://www.quark.cn/s?q="+string,data="")