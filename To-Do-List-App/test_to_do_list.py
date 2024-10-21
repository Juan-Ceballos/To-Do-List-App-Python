import unittest
from datetime import datetime

import to_do_list
import to_do_item

class TestToDoList(unittest.TestCase):

    def test_initialize(self):
        to_do_list_tc = to_do_list.ToDoList({}, "Work", datetime, 0)
        self.assertEqual(len(to_do_list_tc.to_do_items), 0)

    def test_add_item(self):
        to_do_list_tc = to_do_list.ToDoList({}, "Gym", datetime, 1)
        to_do_sample = to_do_item.ToDoItem("Pushups", "10 Reps", "10/15/2024", "2")
        to_do_list_tc.add_to_do(to_do_sample, to_do_sample.to_do_id)
        to_do_list_tc.display_to_dos("2")
        self.assertEqual(len(to_do_list_tc.to_do_items), 1)

    def test_edit_item(self):
        to_do_list_tc = to_do_list.ToDoList({}, "School", datetime, 3)
        to_do_sample = to_do_item.ToDoItem("Math", "10 Integrals", "10/13/2024", 4)
        to_do_result = to_do_list_tc.edit_to_do(to_do_sample)
        self.assertEqual(to_do_result.title, "Math")

    def test_delete_item(self):
        to_do_list_tc = to_do_list.ToDoList({}, "School", datetime, 5)
        to_do_sample = to_do_item.ToDoItem("Math", "10 Integrals", "10/13/2024", 6)
        to_do_result = to_do_list_tc.edit_to_do(to_do_sample)




if __name__ == '__main__':
    unittest.main()
