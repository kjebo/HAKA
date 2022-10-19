from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from ipwhois import IPWhois
import nmap
import re

app = Flask(__name__)
  
@app.route('/<string:ip>')
def get_ip(ip):
    nm = nmap.PortScanner()
    obj = IPWhois(ip)
    results = obj.lookup_rdap(depth=1)
    network_handle = results['network']['handle']
    network_handle_list = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',network_handle)
    last_ip_dress = re.findall('\d{1,3}$',network_handle_list[1])
    scan_this = f'{network_handle_list[0]}-{last_ip_dress[0]}'
    result = nm.scan(hosts=scan_this, arguments='-sP')
    
    print(network_handle_list)
    print(network_handle)

    return results
 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
