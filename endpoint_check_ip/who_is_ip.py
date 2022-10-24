from flask import Flask, request
from ipwhois import IPWhois
import nmap
import re


app = Flask(__name__)
  
@app.route('/<string:ip>')
def get_ip(ip):
    nm = nmap.PortScanner()
    obj = IPWhois(ip)
    whois = obj.lookup_rdap(depth=1)
    range = whois['network']['cidr']
    network_mask = re.findall(r"..$", range)[0] 

    if int(network_mask)  >= 24:
        result = nm.scan(hosts=range, arguments='-sP')
        return result
    else:
        return whois['asn_description']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
