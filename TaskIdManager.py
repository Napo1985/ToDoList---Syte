class TaskIdManager(object):
    """provid uniq Id """
#-----------------------------------------------------------------------------------#
    #this class use a stack to save all removed id's and reuse them if needed.
    def __init__(self):
        self.IdStack = []
        self.m_RunningId = 0
#-----------------------------------------------------------------------------------#
    #get uniq id from the system
    def GetUniqId(self):
        newId= 0
        if not self.IdStack:
            self.m_RunningId += 1
            newId = self.m_RunningId;
        else:
            newId = self.IdStack.pop();
        return newId;
#-----------------------------------------------------------------------------------#
    #retrun a uniq id to the system
    def PutUniqId (self, id):
        self.IdStack.append(id);
#-----------------------------------------------------------------------------------#