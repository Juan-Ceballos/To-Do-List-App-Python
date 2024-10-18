import unittest
import to_do_list
import to_do_item

class TestToDoList(unittest.TestCase):

    def test_initialize(self):
        to_do_list_tc = to_do_list.ToDoList({}, "Work", id)
        self.assertEqual(len(to_do_list_tc.to_do_items), 0)

    def test_add_item(self):
        to_do_list_tc = to_do_list.ToDoList({}, "Gym", id)
        to_do_sample = to_do_item.ToDoItem("Pushups", "10 Reps", "10/15/2024", id)
        to_do_list_tc.add_to_do(to_do_sample, to_do_sample.to_do_id)
        self.assertEqual(len(to_do_list_tc.to_do_items), 1)

    def test_edit_item(self):
        to_do_list_tc = to_do_list.ToDoList({}, "School", id)
        to_do_sample = to_do_item.ToDoItem("Math", "10 Integrals", "10/13/2024", id)
        to_do_result = to_do_list_tc.edit_to_do(to_do_sample)
        self.assertEqual(to_do_result.title, "Math")

    def test_delete_item(self):
        to_do_list_tc = to_do_list.ToDoList({}, "School", id)
        to_do_sample = to_do_item.ToDoItem("Math", "10 Integrals", "10/13/2024", id)
        to_do_result = to_do_list_tc.edit_to_do(to_do_sample)




if __name__ == '__main__':
    unittest.main()
