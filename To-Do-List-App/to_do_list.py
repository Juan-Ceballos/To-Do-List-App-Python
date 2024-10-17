from contextlib import nullcontext


class ToDoList(object):

    def __init__(self, to_do_items, title, category, to_do_list_id):
        self.to_do_items = {}
        self.title = title
        self.category = category
        self.to_do_list_id = id

    def add_to_do(self, to_do_item, to_do_id):
        self.to_do_items[to_do_id] = to_do_item

    @staticmethod
    def edit_to_do(self, to_do_item):
        return to_do_item

    def delete_to_do(self, to_do_id):
        del self.to_do_items[to_do_id]

