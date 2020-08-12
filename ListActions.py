from TaskIdManager import TaskIdManager
from Task import Task
import traceback
import IStorage

class ListActions(object):
    """implement all ToDoList actions"""
    
    def __init__(self,storage,idManager):
        if not isinstance(storage, IStorage.IStorage):
            raise TypeError("storage must inherite from IStorage interface")
        self.m_memory = storage
        self.m_IdManager = idManager

    def AddTaskToList(self, taskDescription):
        try:
            if isinstance(taskDescription, str):
                newtask = Task(taskDescription)
                newtask.m_taskID = self.m_IdManager.GetUniqId()
                if (newtask.m_taskID == None):
                    return False

                self.m_memory.AddTask(newtask.m_taskID,newtask)
                return True
            else:
                return False
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 

    def RemoveTaskFromList (self, id):
        try:
            if self.m_memory.ContainKey(id):
                removed_value = self.m_memory.RemoveTask(id)
                self.m_IdManager.PutUniqId(id)
                return removed_value.m_task
            else:
                return None
        except:
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 

    def RemoveAllTasksFromList (self):
        try:
            for item in self.m_memory.GetAllValues():
                id = item.m_taskID
                self.m_IdManager.PutUniqId(id)
            self.m_memory.RemoveAllTasks()
        except:
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 

    def GetAllTasks (self):
        try:
            tasksList = list(self.m_memory.GetAllValues());
            return tasksList;
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 

    def MarkTaskAsDone(self, id):
        try:
            task = self.m_memory.GetById(id)
            if task != None:
                task.m_isDone = True;
            else:
                return False

            return True
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}')