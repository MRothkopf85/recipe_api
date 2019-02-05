import os
from flask import Flask, request
from flask_restful import Resource, Api
from resources.recipe import Recipe

import psycopg2

db_pass = os.environ["POSTGRES_PASSWORD"]
db_user = os.environ["POSTGRES_USER"]
db_host = os.environ["POSTGRES_HOST"]
app_port = os.environ["PORT"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + db_user + ':' + db_pass + '@' + db_host + '/' + 'postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Recipe, '/recipe/<string:name>')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=app_port, debug=True)
