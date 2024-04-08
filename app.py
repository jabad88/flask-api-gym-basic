from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///gymdb.db"
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return self.name
    
with app.app_context():
    db.create_all()


task_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

class Exercises(Resource):
    @marshal_with(task_fields)
    def get(self):
        exercises = Task.query.all()
        return exercises
    
    @marshal_with(task_fields)
    def post(self):
        data = request.json
        task = Task(name=data["name"])
        db.session.add(task)
        db.session.commit()
        exercises = Task.query.all()

        return exercises

    
class Exercise(Resource):
    @marshal_with(task_fields)
    def get(self,pk):
        exercise = Task.query.filter_by(id=pk).first()
        return exercise


    def put(self,pk):
        data = request.json

        task = Task.query.filter_by(id=pk).first()
        task.name = data['name']
        db.session.commit()
        return task

    
    def delete(self,pk):
        task = Task.query.filter_by(id=pk).first()
        db.session.delete(task)
        db.session.commit()

        exercises = Task.query.all()

        return exercises


api.add_resource(Exercises, '/exercises')
api.add_resource(Exercise, '/<int:pk>')


if __name__ == '__main__':
    app.run(debug=True)