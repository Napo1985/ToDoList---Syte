import flask
from flask import request, jsonify
from ListActions import ListActions
from TaskConvertor import TaskConvertor
import MemoryStorage
import TaskIdManager

list = ListActions(MemoryStorage.MemoryStorage(), TaskIdManager.TaskIdManager())
list.AddTaskToList("CALL doctor")
list.AddTaskToList("Wash Car")

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/tasks', methods=['GET'])
def AllTasks():
    alltasks = list.GetAllTasks()
    taskAsStrlist = []
    for item in alltasks:
        taskAsStrlist.append(TaskConvertor().ConvertTaskToString(item))
    return jsonify({'alltasks' : taskAsStrlist})

# curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/tasks/task3
@app.route('/tasks/<string:new_task>', methods=['POST'])
def CreateTask(new_task):
    if list.AddTaskToList(new_task):
        return jsonify({'addNewTask' : "task - " + new_task + " added to the list"})
    else:
        return jsonify({'Error' : "task - " + new_task + " was not added to the list"})

# curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/tasks/id
@app.route('/tasks/<int:id>', methods=['DELETE'])
def DeleteTask(id):
    taskDescription = list.RemoveTaskFromList(id)
    if taskDescription != None:
        return jsonify({'task removed' : "task - " + taskDescription + " removed from the list"})
    else:
        return jsonify({'Error' : "task with id - " + str(id) + " was not removed from the list"})

# curl -i -H "Content-Type: application/json" -X PUT http://localhost:5000/tasks/id
@app.route('/tasks/<int:id>', methods=['PUT'])
def MarkTaskAsDone(id):
    retBool = list.MarkTaskAsDone(id)
    if retBool:
        return jsonify({'task update' : "task with id " + str(id) + " was updated"})
    else:
        return jsonify({'task update' : "id - " + str(id) + " was not found"})

app.run()