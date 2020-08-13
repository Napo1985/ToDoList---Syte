import traceback
import IIdManager

class TaskIdManager(IIdManager.IIdManager):
    """this class Providing a uniq id using in memory data structure"""

    def __init__(self):
        self.IdStack = []
        self.m_RunningId = 0

    #Returns a uniq id of type int
    #Function logic - check if there is a reusable id to return,if not it will generate a new unique id
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

    #Store unused unique ids
    def PutUniqId (self, id):
        try:
            self.IdStack.append(id);
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 
