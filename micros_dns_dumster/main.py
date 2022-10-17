import os

DOMAIN = 'cfigroup.se'

os.system(f'python3 dns_dumster.py -d {DOMAIN} -i data/only_ip.txt -o data/all_info.txt')

