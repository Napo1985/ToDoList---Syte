import abc

class IIdManager(metaclass=abc.ABCMeta):
    """description of class"""

    @abc.abstractmethod
    def GetUniqId(self):
        pass

    @abc.abstractmethod
    def PutUniqId(self,id):
        pass


