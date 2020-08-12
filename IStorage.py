import abc

class IStorage(metaclass=abc.ABCMeta):
    """description of class"""
    @abc.abstractmethod
    def AddTask(self,id,task):
        pass

    @abc.abstractmethod
    def RemoveTask(self,id):
        pass
    
    @abc.abstractmethod
    def RemoveAllTasks(self):
        pass
    
    @abc.abstractmethod
    def GetAllValues(self):
        pass

    @abc.abstractmethod
    def GetById(self,id):
        pass

    @abc.abstractmethod
    def ContainKey(self,id):
        pass
