import re
lst = []
with open("data_files/all_info.txt", 'r') as f:

    for line in f.readlines():
        d = dict(line.split("=") for x in line.split())
        for k, v in d.items():
            my_dict = {k:v.strip()}
        lst.append(my_dict)
 
print(lst)