from flask import Flask, request, render_template
from curses import keyname
import requests
from pprint import pprint

#BASE = "http://localhost:5001/" # Check ip adresses
BASE = "http://localhost:5002/" # Check domainnames
DB = "http://localhost:5003/my_response" #Database


app = Flask(__name__)  
s = requests.Session()


@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       ip = request.form.get("Domain")
       my_response = requests.get(BASE + ip)
       s.get(url=DB,data=my_response)
       
       return my_response.json()
    return render_template("form.html")

 
if __name__=='__main__':
   app.run(host='localhost', port=5000, debug=True)

