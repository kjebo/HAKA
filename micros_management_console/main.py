# importing Flask and other modules
from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       ip = request.form.get("ip")
       # getting input with name = lname in HTML form
       domain = request.form.get("domain")
       return "Result: "+ ip + domain
    return render_template("form.html")
 
if __name__=='__main__':
   app.run(host='localhost', port=5500, debug=True)