#public import
from flask_restful import marshal_with, Resource
from flask import request, jsonify

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
        if "name" not in data:
            return {"message": "Missing required field: 'Name'"}, 400
        task = Task()
        task.name = data['name']
        db.session.add(task)
        db.session.commit()
        return {"id":task.id, "name":task.name}, 201
    
class Exercise(Resource):
    @marshal_with(task_fields)
    def get(self,pk):
        exercise = Task.query.filter_by(id=pk).first()
        #TODO: Still returning null on improper id
        if not exercise:
            return {"message":"There is no exercise with that ID"}, 404
        return exercise.to_dict()

    @marshal_with(task_fields)
    def put(self,pk):
        data = request.json
        task = Task.query.filter_by(id=pk).first()
        if not task:
            return {"message":"There is no exercise with that ID"}, 404
        task.name = data['name']
        db.session.commit()
        return task

    @marshal_with(task_fields)
    def delete(self,pk):
        task = Task.query.filter_by(id=pk).first()
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": f"Deleted the exercise with task id {pk}"})
    