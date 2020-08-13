from Task import Task
import traceback
import IStorage
import IIdManager
import logging

class ListActions(object):
    """implement all ToDoList actions"""
    

    #paramters:
    #storage - A class that derives from IStorage interface
    #idManager - A class that derives from IIdManager interface
    def __init__(self,storage,idManager):
        log = "app.log"
        logging.basicConfig(filename=log,level=logging.DEBUG ,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
        
        if not isinstance(storage, IStorage.IStorage):
            logging.warning(f'storage must inherite from IStorage interface')
            raise TypeError("storage must inherite from IStorage interface")
        if not isinstance(idManager, IIdManager.IIdManager):
            logging.warning(f'idManager must inherite from IIdManager interface')
            raise TypeError("idManager must inherite from IIdManager interface")

        self.m_memory = storage
        self.m_IdManager = idManager
        logging.info('Init list actions')
    
    #paramters:
    # taskDescription - A string with the todo task description
    def AddTaskToList(self, taskDescription):
        try:
            if isinstance(taskDescription, str):
                newtask = Task(taskDescription)
                newtask.m_taskID = self.m_IdManager.GetUniqId()
                if (newtask.m_taskID == None):
                    return False

                self.m_memory.AddTask(newtask.m_taskID,newtask)
                logging.info(f'task id - {newtask.m_taskID} added to the list')
                return True
            else:
                logging.warning(f'taskDescription is not str type')
                return False
        except :
            tb = traceback.format_exc()
            logging.exception(f'EXCEPTION {tb}')

    #paramters:
    # id - An int of a specific todo task
    def RemoveTaskFromList (self, id):
        try:
            if self.m_memory.ContainKey(id):
                removed_value = self.m_memory.RemoveTask(id)
                self.m_IdManager.PutUniqId(id)
                logging.info(f'task id - {id} removed from the list')
                return removed_value.m_task
            else:
                logging.warning(f'task id - {id} not found')
                return None
        except:
            tb = traceback.format_exc()
            logging.exception(f'EXCEPTION {tb}')
  

    
    def RemoveAllTasksFromList (self):
        try:
            for item in self.m_memory.GetAllValues():
                id = item.m_taskID
                self.m_IdManager.PutUniqId(id)
            self.m_memory.RemoveAllTasks()
            logging.info(f'cleared list')
        except:
            tb = traceback.format_exc()
            logging.exception(f'EXCEPTION {tb}') 

                
    def GetAllTasks (self):
        try:
            tasksList = list(self.m_memory.GetAllValues());
            return tasksList;
        except :
            tb = traceback.format_exc()
            logging.exception(f'EXCEPTION {tb}') 

    #paramters:
    # id - An int of a specific todo task
    def MarkTaskAsDone(self, id):
        try:
            task = self.m_memory.GetById(id)
            if task != None:
                task.m_isDone = True;
            else:
                logging.warning(f'task id - {id} did not marked as done')
                return False
            logging.info(f'task id - {id} marked as done')
            return True
        except :
            tb = traceback.format_exc()
            logging.exception(f'EXCEPTION {tb}') 