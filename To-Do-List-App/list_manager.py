from pydoc import describe

from to_do_list import ToDoList


class ListManager:

    all_lists = {}

    def __init__(self):
        pass

    @classmethod
    def add_list(cls, to_do_list, list_title):
        cls.all_lists[list_title] = to_do_list