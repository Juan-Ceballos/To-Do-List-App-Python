from datetime import datetime
import uuid

class ToDoItem(object):
    def __init__(self, description, due_date):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        self.description = description
        self.date_created = dt_string
        self.due_date = due_date
        self.to_do_id = uuid.uuid1()
