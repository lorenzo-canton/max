import socket
import requests
import json
import datetime
import os

x = datetime.datetime.now()

url = 'http://192.168.1.56:8081/?title='
hostname = socket.getfqdn()
data = json.loads(requests.get("https://ip.seeip.org/jsonip?").text)["ip"]
requests.post(url + 'public-' + x.strftime("%H-%M-%d-%m-%Y"), data)
print (data)

stream = os.popen('nmap 192.168.1.1/24')
output = stream.read()
requests.post(url + 'scan-' + x.strftime("%H-%M-%d-%m-%Y"), output)
print(output)