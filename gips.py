import socket
import requests
import json

url = 'http://192.168.1.24:8081/?title=test'

hostname = socket.getfqdn()

data = json.loads(requests.get("https://ip.seeip.org/jsonip?").text)["ip"]

x = requests.post(url, data)

print (data)
print(x.text)
