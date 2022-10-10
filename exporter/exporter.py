from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api =Api(app)

class dns_dump(Resource):
    def get(self, name, status):
        return {"name": name, "status":status}

api.add_resource(dns_dump, "/hello/<string:name>/<string:status>")


if __name__ =="__main__":
    app.run(debug=True)
