'''
1. Using whois command to check if the targetcompany have more ipadresses. 
The whois result is saved in the database.
2. Using regex to capture the ipadresses and nmap -sP command to check if targets are up and running
'''

from ipwhois import IPWhois
import nmap
import re

nm = nmap.PortScanner()

#ip = "62.63.215.64"
ip = "193.15.26.122"
obj = IPWhois(ip)
results = obj.lookup_rdap(depth=1)

network_handle = results['network']['handle']
network_handle_list = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',network_handle)
last_ip_dress = re.findall('\d{1,3}$',network_handle_list[1])

scan_this = f'{network_handle_list[0]}-{last_ip_dress[0]}'
nm.scan(hosts=scan_this, arguments='-sP')

print(nm.all_hosts())
with open('ip.txt','a') as f:
    for item in nm.all_hosts():
        f.write(item)
        f.write('\n')
hosts_list = [(x, nm[x]['status']) for x in nm.all_hosts()]
print(hosts_list)

print(scan_this)