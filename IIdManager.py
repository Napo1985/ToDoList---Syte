import abc

class IIdManager(metaclass=abc.ABCMeta):
    """Interface class for all uniq id providers"""

    @abc.abstractmethod
    def GetUniqId(self):
        pass

    @abc.abstractmethod
    def PutUniqId(self,id):
        pass


