import unittest
import ListActions 
import MemoryStorage 
import TaskIdManager
from Task import Task


class Test_test_ListActions(unittest.TestCase):

    def setUp(self):
        self.list =ListActions.ListActions(MemoryStorage.MemoryStorage(),TaskIdManager.TaskIdManager())
    
    def tearDown(self):
        self.list.RemoveAllTasksFromList()



    def test_EmptyList(self):
        retval = self.list.GetAllTasks()
        self.assertTrue( len(retval) == 0)

    def test_AddItemToList(self):
        taskstring = "first task"
        self.list.AddTaskToList(taskstring)
        retval = self.list.GetAllTasks()

        self.assertTrue( len(retval) == 1)
        self.assertTrue( retval[0].m_taskID == 1)
        self.assertTrue( retval[0].m_task == taskstring)

    def test_AddIEmptytemToList(self):
        #list = ListActions()
        retbool = self.list.AddTaskToList("")
        retval = self.list.GetAllTasks()
        self.assertTrue( retval[0].m_task == "empty task")

    def test_RemoveItemFromList(self):
        #list = ListActions()
        taskstring = "first task"
        self.list.AddTaskToList(taskstring)
        self.list.RemoveTaskFromList(1)
        retval = self.list.GetAllTasks()
        self.assertTrue( len(retval) == 0)

    def test_UniqIdReuse(self):
        #list = ListActions()
        taskstring = "first task"
        self.list.AddTaskToList(taskstring)
        self.list.RemoveAllTasksFromList()
        self.list.AddTaskToList(taskstring)
        retval = self.list.GetAllTasks()
        self.assertTrue( retval[0].m_taskID == 1)

    def test_ChangeDoneFlageInTask(self):
        #list = ListActions()
        taskstring = "first task"
        self.list.AddTaskToList(taskstring)
        self.list.MarkTaskAsDone(1)
        retval = self.list.GetAllTasks()
        self.assertTrue( retval[0].m_isDone == True)

    def test_ClearList(self):
        #list = ListActions()
        taskstring = "first task"
        self.list.AddTaskToList(taskstring)
        self.list.RemoveAllTasksFromList()
        retval = self.list.GetAllTasks()
        self.assertTrue(len(retval) == 0)

    def test_ClearEmptyList(self):
        #list = ListActions()
        self.list.RemoveAllTasksFromList()
        retval = self.list.GetAllTasks()
        self.assertTrue(len(retval) == 0)
        
if __name__ == '__main__':
    unittest.main()

