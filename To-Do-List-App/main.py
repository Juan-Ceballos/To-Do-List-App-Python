from datetime import datetime
from list_manager import ListManager
import to_do_list
import uuid
from to_do_list import ToDoList


def display_lists(lists):
    if len(lists) == 0:
        print("Empty")
    for single_list in lists:
        print("-" + " " + single_list)

def query_list():
    selected_category = input("Type list you want to select or type a new list to start creating: ")
    if selected_category in ListManager.all_lists:
        # not expecting string for key
        select_list()
    else:
        create_new_list(selected_category)

def create_new_list(title_input):
    print("creating new list: " + title_input)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    list_id = uuid.uuid1()
    new_list = to_do_list.ToDoList({}, title_input, dt_string, list_id)
    ListManager.add_list(new_list, new_list.title)
    print("Displaying all to do lists")
    display_lists(ListManager.all_lists)

def select_list():
    print("selecting list: some list")


def main():
    print("called main")
    display_lists(ListManager.all_lists)
    query_list()

if __name__ == '__main__':
    main()