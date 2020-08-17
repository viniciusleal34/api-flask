from flask import Flask
from flask_restful  import Api
from src.registro import Registro
from flask_cors import CORS
import os

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})
api = Api(app)
api.add_resource(Registro,'/home')



def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1",port=port, debug=True)

if __name__ == "__main__":
    main()