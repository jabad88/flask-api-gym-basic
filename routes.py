#public import
from flask_restful import marshal_with, Resource
from flask import request

#local import
from models import Task
from db import db
from schemas import task_fields

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