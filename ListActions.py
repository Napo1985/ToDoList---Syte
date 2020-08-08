import TaskIdManager
import Task

class ListActions(object):
    """implement all ToDoList actions"""
    
#-----------------------------------------------------------------------------------#
    #get this out of this class and use dependency injection
    #m_taskDictionry  
    #m_taskIdManager 
#-----------------------------------------------------------------------------------#
    def __init__(self):
        self.m_taskDictionry = dict()
        self.m_taskIdManager = TaskIdManager.TaskIdManager();
#-----------------------------------------------------------------------------------#
    # addToList - provide the Task
    def AddTaskToList(self, task):
        if isinstance(task, Task.Task):
            task.m_taskID = self.m_taskIdManager.GetUniqId()
            self.m_taskDictionry[task.m_taskID] = task;
            return True;
        else:
            return False;
#-----------------------------------------------------------------------------------#
    #removeTaskFromList - provid ID
    def RemoveTaskFromList (self, id):
         if id in self.m_taskDictionry:
             removed_value = self.m_taskDictionry.pop(id)
             self.m_taskIdManager.PutUniqId(id)
#-----------------------------------------------------------------------------------#
    def GetAllTasks (self):
        tasksList = list(self.m_taskDictionry.values());
        return tasksList;
#-----------------------------------------------------------------------------------#
    def MarkTaskAsDone(self, id):
        if id in m_taskDictionry:
            task = m_taskDictionry[id];
            task.m_isDone = True;
#-----------------------------------------------------------------------------------#
    def MarkTaskAsUnDone(id):
        if id in m_taskDictionry:
            task = m_taskDictionry[id];
            task.m_isDone = False;
#-----------------------------------------------------------------------------------#