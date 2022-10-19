from flask import Flask, jsonify, request
from ipwhois import IPWhois
import nmap
import re

nm = nmap.PortScanner()


#ip = "62.63.215.64"
ip = "193.15.26.122"

# Using Whois to check the IP-address
obj = IPWhois(ip)
results = obj.lookup_rdap(depth=1)

# Grepping info about network handle from the whois result
network_handle = results['network']['handle']
network_handle_list = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',network_handle)
last_ip_dress = re.findall('\d{1,3}$',network_handle_list[1])
scan_this = f'{network_handle_list[0]}-{last_ip_dress[0]}'

# Doing a ping scan on the on All IPs
nm.scan(hosts=scan_this, arguments='-sP')

app = Flask(__name__)

ip_addr = [
    { 'IP-address': nm.all_hosts()}
]

''''''
@app.route('/')
def get_ip():
    return jsonify(ip_addr)


@app.route('/', methods=['POST'])
def check_ip():
    ip_addr.append(request.get_json())
    return '', 204


if __name__ =="__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)