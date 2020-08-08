import ListActions
import Task
import time

theList = ListActions.ListActions();

task1 = Task.Task("yaniv");
time.sleep(1)
task2 = Task.Task("miri");

theList.AddTaskToList(task1);
theList.AddTaskToList(task2);

theList.RemoveTaskFromList(1)
time.sleep(1)
task3 = Task.Task("Romi")
theList.AddTaskToList(task3);

allTheTaskes =  theList.GetAllTasks();

for item in allTheTaskes: 
    print(item.m_taskID, "|", item.m_task, "|", item.m_timeStemp, "|", item.m_isDone);