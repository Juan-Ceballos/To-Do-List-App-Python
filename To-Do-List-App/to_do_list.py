from datetime import datetime
import uuid


class ToDoList(object):

    def __init__(self, to_do_items, title):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        self.to_do_items = to_do_items
        self.title = title
        self.date_edited = dt_string
        self.to_do_list_id = uuid.uuid1()

    def add_to_do(self, to_do_item, to_do_id):
        self.to_do_items[to_do_id] = to_do_item

    def delete_to_do(self, to_do_id):
        del self.to_do_items[to_do_id]