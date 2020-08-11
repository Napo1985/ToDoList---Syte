import flask
from flask import request, jsonify
from ListActions import ListActions
from TaskConvertor import TaskConvertor

list = ListActions()
list.AddTaskToList("CALL doctor")
list.AddTaskToList("Wash Car")

app = flask.Flask(__name__)
app.config["DEBUG"] = True



#-----------------------------------------------------------------------------------#
@app.route('/tasks', methods=['GET'])
def AllTasks():
    alltasks = list.GetAllTasks()
    taskAsStrlist = []
    for item in alltasks:
        taskAsStrlist.append(TaskConvertor().ConvertTaskToString(item))
    return jsonify({'alltasks' : taskAsStrlist})
#-----------------------------------------------------------------------------------#
#@app.route('/tasks/<int:task_id>', methods=['GET']) #TODO add func with id and get him.
#def TaskById(task_id):
#    retTask = None
#    alltasks = list.GetAllTasks()
#    for taskItem in alltasks:
#        if taskItem.m_taskID == task_id:
#            retTask = taskItem

#    if retTask != None:
#        return jsonify({'alltasks' : list.ConvertTaskToString(retTask)})
#    else:
#        return jsonify({'alltasks' : "Id not found"})
#-----------------------------------------------------------------------------------#
# curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/tasks/task3
@app.route('/tasks/<string:new_task>', methods=['POST'])
def CreateTask(new_task):
    list.AddTaskToList(new_task)
    return jsonify({'addNewTask' : "task - " + new_task + " added to the list"})

# curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/tasks/id
@app.route('/tasks/<int:id>', methods=['DELETE'])
def DeleteTask(id):
    taskDescription = list.RemoveTaskFromList(id)
    return jsonify({'task removed' : "task - " + taskDescription + " removed from  the list"})

# curl -i -H "Content-Type: application/json" -X PUT http://localhost:5000/tasks/id
@app.route('/tasks/<int:id>', methods=['PUT'])
def MarkTaskAsDone(id):
    retBool = list.MarkTaskAsDone(id)
    if retBool:
        return jsonify({'task update' : "task with id " + str(id) + " was updated"})
    else:
        return jsonify({'task update' : "id - " + str(id) + " was not found"})

app.run()