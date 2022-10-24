from flask import Flask, request
import re
import os


app = Flask(__name__)
list = []  
@app.route('/<string:domain>')
def get_ip(domain):
    os.system(f'python3 dns_dumster.py -d {domain} -i data_files/only_ip.txt -o data_files/all_info.txt')
    lst = []
    
    with open("data_files/all_info.txt", 'r') as f:

        for line in f.readlines():
            d = dict(line.split("=") for x in line.split())
            for k, v in d.items():
                my_dict = {k:v.strip()}
            lst.append(my_dict)
    
    return {domain:lst}
 
 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)