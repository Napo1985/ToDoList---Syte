import unittest
from ListActions import ListActions
from Task import Task

class Test_test_ListActions(unittest.TestCase):
    
        #def test_Tamplate(self):
        #    list = ListActions()
        #    retval = list.GetAllTasks()

        #    self.assertTrue( )
    
    #def setUp(self):
    #    list = ListActions()
    #    pass
    
    #def tearDown(self):
    #    pass



    def test_EmptyList(self):
        list = ListActions()
        retval = list.GetAllTasks()
        self.assertTrue( len(retval) == 0)

    def test_AddItemToList(self):
        list = ListActions()
        taskstring = "first task"
        list.AddTaskToList(taskstring)
        retval = list.GetAllTasks()

        self.assertTrue( len(retval) == 1)
        self.assertTrue( retval[0].m_taskID == 1)
        self.assertTrue( retval[0].m_task == taskstring)

    def test_AddIEmptytemToList(self):
        list = ListActions()
        retbool = list.AddTaskToList("")
        retval = list.GetAllTasks()
        self.assertTrue( retval[0].m_task == "empty task")

    def test_RemoveItemFromList(self):
        list = ListActions()
        taskstring = "first task"
        list.AddTaskToList(taskstring)
        list.RemoveTaskFromList(1)
        retval = list.GetAllTasks()
        self.assertTrue( len(retval) == 0)

    def test_UniqIdReuse(self):
        list = ListActions()
        taskstring = "first task"
        list.AddTaskToList(taskstring)
        list.RemoveAllTasksFromList()
        list.AddTaskToList(taskstring)
        retval = list.GetAllTasks()
        self.assertTrue( retval[0].m_taskID == 1)

    def test_ChangeDoneFlageInTask(self):
        list = ListActions()
        taskstring = "first task"
        list.AddTaskToList(taskstring)
        list.MarkTaskAsDone(1)
        retval = list.GetAllTasks()
        self.assertTrue( retval[0].m_isDone == True)

    def test_ClearList(self):
        list = ListActions()
        taskstring = "first task"
        list.AddTaskToList(taskstring)
        list.RemoveAllTasksFromList()
        retval = list.GetAllTasks()
        self.assertTrue(len(retval) == 0)

    def test_ClearEmptyList(self):
        list = ListActions()
        list.RemoveAllTasksFromList()
        retval = list.GetAllTasks()
        self.assertTrue(len(retval) == 0)
        
if __name__ == '__main__':
    unittest.main()

