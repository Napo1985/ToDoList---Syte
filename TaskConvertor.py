from Task import Task
class TaskConvertor(object):
    """Convert Task class into a string"""

    def ConvertTaskToString(self, task):
        try:
            if isinstance(task, Task):
                taskAsStr = f'{task.m_taskID} | {task.m_task} | {task.m_timeStemp} | {task.m_isDone}'
                return taskAsStr
        except :
            tb = traceback.format_exc()
            print (f'EXCEPTION {tb}') 

