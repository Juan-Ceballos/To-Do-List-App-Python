class ToDoList(object):

    def __init__(self, to_do_items, title, date_edited, to_do_list_id):
        self.to_do_items = to_do_items
        self.title = title
        self.date_edited = date_edited
        self.to_do_list_id = to_do_list_id

    def add_to_do(self, to_do_item, to_do_id):
        self.to_do_items[to_do_id] = to_do_item

    def delete_to_do(self, to_do_id):
        del self.to_do_items[to_do_id]