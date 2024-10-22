import unittest
from datetime import datetime

import list_manager
import to_do_list

class TestListManager(unittest.TestCase):

    def test_initialization(self):
        list_manager_tc = list_manager.ListManager()
        self.assertEqual(len(list_manager_tc.all_lists), 0)

    def test_manager_add_list(self):
        to_do_list_tc = to_do_list.ToDoList({}, "Gym", datetime, id)
        to_do_list_tc2 = to_do_list.ToDoList({}, "School", datetime, id)
        list_manager.ListManager.add_list(to_do_list_tc, to_do_list_tc.title)
        list_manager.ListManager.add_list(to_do_list_tc2, to_do_list_tc2.title)
        self.assertEqual(len(list_manager.ListManager.all_lists), 2)

if __name__ == '__main__':
    unittest.main()