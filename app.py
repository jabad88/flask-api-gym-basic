from flask import Flask
from flask_restful import Api
from db import db
from routes import Exercises, Exercise

app = Flask(__name__)
api = Api(app)

# Load configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/josh/Documents/flask_gym/instance/gymdb.db"

db.init_app(app)


# Register API endpoints
api.add_resource(Exercises, '/exercises')
api.add_resource(Exercise, '/<int:pk>')

if __name__ == '__main__':
    app.run(debug=True)