from flask_restful import Api, Resource
from flask import Flask
from getdata import GetJson


app = Flask(__name__)
api = Api(app)

data = GetJson()
class GetMedical(Resource):
    def get(self,symtoms):
        symtoms = symtoms.split("+")
        symtoms = ' '.join(symtoms)

        results = data.search(symtoms=symtoms)

        return {"results": results}

    def post(self):
        return {"this is json serialized":"post"}


api.add_resource(GetMedical, "/<string:symtoms>")

if __name__ == "__main__":
    app.run(debug=False, port=8000)

