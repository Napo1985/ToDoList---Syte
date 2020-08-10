from TaskIdManager import TaskIdManager
from Task import Task
import traceback


class ListActions(object):
    """implement all ToDoList actions"""
    
#-----------------------------------------------------------------------------------#
    #get this out of this class and use dependency injection
    #m_taskDictionry  
    #m_taskIdManager 
#-----------------------------------------------------------------------------------#
    def __init__(self):
        self.m_taskDictionry = dict()
        self.m_taskIdManager = TaskIdManager();
#-----------------------------------------------------------------------------------#
    # addToList - provide the Task
    def AddTaskToList(self, taskDescription):
        try:
            if isinstance(taskDescription, str):
                newtask = Task(taskDescription)
                newtask.m_taskID = self.m_taskIdManager.GetUniqId()
                if (newtask.m_taskID == None):
                    return False

                self.m_taskDictionry[newtask.m_taskID] = newtask;
                return True;
            else:
                return False;
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 
#-----------------------------------------------------------------------------------#
    #removeTaskFromList - provid ID
    def RemoveTaskFromList (self, id):
        try:
            if id in self.m_taskDictionry:
                removed_value = self.m_taskDictionry.pop(id)
                self.m_taskIdManager.PutUniqId(id)
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 
#-----------------------------------------------------------------------------------#
    def RemoveAllTasksFromList (self):
        try:
            for item in self.m_taskDictionry.values():
                id = item.m_taskID
                self.m_taskIdManager.PutUniqId(id)
            self.m_taskDictionry.clear()
        except:
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 
#-----------------------------------------------------------------------------------#
    def GetAllTasks (self):
        try:
            tasksList = list(self.m_taskDictionry.values());
            return tasksList;
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 
#-----------------------------------------------------------------------------------#
    def MarkTaskAsDone(self, id):
        try:
            task = self.m_taskDictionry.get(id,None)
            if task != None:
                task.m_isDone = True;
            else:
                return False

            return True
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 

#-----------------------------------------------------------------------------------#
    def MarkTaskAsUnDone(self, id):
        try:
            task = self.m_taskDictionry.get(id,None)
            if task != None:
                task.m_isDone = False
            else:
                return False;
            return True
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 
#-----------------------------------------------------------------------------------#
    def ConvertTaskToString(self, task):
        try:
            if isinstance(task, Task):
               taskAsStr = f'{task.m_taskID} | {task.m_task} | {task.m_timeStemp} | {task.m_isDone}'
               return taskAsStr
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 

#-----------------------------------------------------------------------------------#