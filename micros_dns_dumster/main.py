from flask import Flask, request
import pandas as pd
import os


app = Flask(__name__)
  
@app.route('/<string:domain>')
def get_ip(domain):
    os.system(f'python3 dns_dumster.py -d {domain} -i data_files/only_ip.txt -o data_files/all_info.txt')
    with open('data_files/all_info.txt','r') as f:
        ip_list = [line.strip('\n') for line in f]
    result = {domain:ip_list}
    return result
    

 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)