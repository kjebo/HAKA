from flask import Flask, request, render_template
from curses import keyname
import requests
from pprint import pprint

#BASE = "http://localhost:5001/" # Check ip adresses
BASE = "http://localhost:5002/" # Check domainnames

app = Flask(__name__)  
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       ip = request.form.get("Domain")
       response = requests.get(BASE + ip)
       return response.json()
    return render_template("form.html")

 
if __name__=='__main__':
   app.run(host='localhost', port=5000, debug=True)

