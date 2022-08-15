import socket
import requests
import json
import datetime

x = datetime.datetime.now()

url = 'http://192.168.1.56:8081/?title=public-' + x.strftime("%H-%M-%d-%m-%Y")

hostname = socket.getfqdn()

data = json.loads(requests.get("https://ip.seeip.org/jsonip?").text)["ip"]

x = requests.post(url, data)

print (data)
print(x.text)
