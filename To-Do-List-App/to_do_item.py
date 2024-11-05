from datetime import datetime
import uuid

class ToDoItem(object):
    def __init__(self, description):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        self.description = description
        self.date_created = dt_string
        self.to_do_id = uuid.uuid1()
