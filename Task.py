import datetime

class Task(object):
    """Task class holding the data input from the user"""
    # m_task will display "empty task" if the user had not enterd data

    def __init__(self, taskToDo):
        self.m_isDone = False;
        self.m_taskID = None;
        self.m_timeStemp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S");

        if (taskToDo == ""):
            self.m_task = "empty task";
        else:
            self.m_task = taskToDo;       



    
        

