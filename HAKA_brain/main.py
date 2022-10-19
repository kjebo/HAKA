from flask import Flask, request, render_template
from curses import keyname
import requests
from pprint import pprint

BASE = "http://127.0.0.1:5000/" 

app = Flask(__name__)  
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       ip = request.form.get("ip")
       # getting input with name = lname in HTML form
       domain = request.form.get("domain")
       response = requests.get(BASE + ip)
       return response.json()
    return render_template("form.html")

 
if __name__=='__main__':
   app.run(host='localhost', port=5500, debug=True)

