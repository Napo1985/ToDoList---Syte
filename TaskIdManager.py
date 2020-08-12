import traceback
import IIdManager

class TaskIdManager(IIdManager.IIdManager):
    """provid uniq Id """

    #this class use a stack to save all removed id's and reuse them if needed.

    def __init__(self):
        self.IdStack = []
        self.m_RunningId = 0

    def GetUniqId(self):
        try:
            newId= 0
            if not self.IdStack:
                self.m_RunningId += 1
                newId = self.m_RunningId;
            else:
                newId = self.IdStack.pop();
            return newId;
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 

    def PutUniqId (self, id):
        try:
            self.IdStack.append(id);
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 
