from ipaddress import ip_address
import os

with open ('ip.txt', 'r') as f:
    ip_adresses = [line.strip() for line in f]

for ip in ip_adresses: 
     os.system(f'wget https://rdap.apnic.net/ip/{ip}')