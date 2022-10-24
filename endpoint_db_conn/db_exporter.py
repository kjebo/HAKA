
from pymongo import MongoClient
from flask import Flask, request

app = Flask(__name__)
  
@app.route('/<my_response>', methods =["GET", "POST"])
def gfg(my_response):
   if request.method == "GET":
      client = MongoClient('localhost', 27017)
      db = client['HAKA']
      coll = db['testing']
      coll.insert_one({"_id":my_response})

      return {"_id":my_response}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)