import IStorage 

class MemoryStorage(IStorage.IStorage):
    """description of class"""
    def __init__ (self):
        self.m_taskDictionry = dict()

    def AddTask(self,id,task):
        self.m_taskDictionry[id] = task;     

    def RemoveTask(self,id):
        return self.m_taskDictionry.pop(id)

    def RemoveAllTasks(self):
        self.m_taskDictionry.clear()

    def GetAllValues(self):
        return self.m_taskDictionry.values()

    def GetById(self,id):
        return self.m_taskDictionry.get(id,None)

    def ContainKey(self,id):
        if id in self.m_taskDictionry:
            return True
        else:
            return False



