#!/bin/bash
#nmap --script vuln [ip]
#   -A  all
$DATA=$(date '+%H-%M-%d-%m-%Y');
python3 gips.py &&
nmap $1 > nscan.txt &&
base64 nscan.txt > nscane.txt &&
curl -d @nscane.txt -X POST http://192.168.1.24:8081?title=scan-$DATA&e=true;
