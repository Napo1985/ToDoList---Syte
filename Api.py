import flask
from flask import request, jsonify
from ListActions import ListActions

list = ListActions()
list.AddTaskToList("CALL doctor")
list.AddTaskToList("Wash Car")

app = flask.Flask(__name__)
app.config["DEBUG"] = True



#-----------------------------------------------------------------------------------#
@app.route('/alltasks', methods=['GET'])
def AllTasks():
    alltasks = list.GetAllTasks()
    taskAsStrlist = []
    for item in alltasks:
        taskAsStrlist.append(list.ConvertTaskToString(item))
    return jsonify({'alltasks' : taskAsStrlist})
#-----------------------------------------------------------------------------------#
@app.route('/alltasks/<int:task_id>', methods=['GET']) #TODO add func with id and get him.
def TaskById(task_id):
    retTask = None
    alltasks = list.GetAllTasks()
    for taskItem in alltasks:
        if taskItem.m_taskID == task_id:
            retTask = taskItem

    if retTask != None:
        return jsonify({'alltasks' : list.ConvertTaskToString(retTask)})
    else:
        return jsonify({'alltasks' : "Id not found"})
#-----------------------------------------------------------------------------------#
# curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/createnewtask/task3
@app.route('/createnewtask/<string:new_task>', methods=['POST'])
def CreateTask(new_task):
    list.AddTaskToList(new_task)
    return jsonify({'addNewTask' : "task - {new_task} added to the list"})

app.run()


