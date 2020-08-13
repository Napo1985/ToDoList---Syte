import flask
from flask import jsonify
from flask import request
from json import JSONEncoder
from ListActions import ListActions
from TaskConvertor import TaskConvertor
import MemoryStorage
import TaskIdManager

list = ListActions(MemoryStorage.MemoryStorage(), TaskIdManager.TaskIdManager())

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/tasks', methods=['GET'])
def AllTasks():
    alltasks = list.GetAllTasks()
    taskAsStrlist = []
    for item in alltasks:
        taskAsStrlist.append(TaskConvertor().ConvertTaskToString(item))
    return jsonify({'list' :taskAsStrlist}),200

# curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/tasks/task3
@app.route('/tasks/<string:new_task>', methods=['POST'] )
def CreateTask(new_task):
    if list.AddTaskToList(new_task):
        return flask.Response(status=201)
    else:
        return flask.Response(status=500)

# curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/tasks/id
@app.route('/tasks/<int:id>', methods=['DELETE'])
def DeleteTask(id):
    taskDescription = list.RemoveTaskFromList(id)
    if taskDescription != None:
        return flask.Response(status=200)
    else:
        return flask.Response(status=500)

# curl -i -H "Content-Type: application/json" -X PUT http://localhost:5000/tasks/id
@app.route('/tasks/<int:id>', methods=['PUT'])
def MarkTaskAsDone(id):
    retBool = list.MarkTaskAsDone(id)
    if retBool:
        return flask.Response(status=200)
    else:
        return flask.Response(status=500)

app.run()