from datetime import datetime
import to_do_item
from list_manager import ListManager
import to_do_list
from to_do_item import ToDoItem
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
        select_list(selected_category)
    else:
        create_new_list(selected_category)


def add_to_dos(curr_list):
    description_inquiry = input("Please add to do description or enter /f to finish: ")
    if description_inquiry != "/f":

        curr_to_do = to_do_item.ToDoItem()
        curr_list.add_to_do()



def create_new_list(title_input):
    print("creating new list: " + title_input)
    now = datetime.now()
    add_to_do_inquiry = input("Add To Dos Now? (y/n): ")
    new_list = to_do_list.ToDoList({}, title_input)
    if add_to_do_inquiry == "y":
        add_to_dos(new_list)

    if to_do_input.lower() != "exit":
        new_list.add_to_do(to_do_input, new_list.to_do_list_id)


    ListManager.add_list(new_list, new_list.title)
    print("Displaying all to do lists")
    display_lists(ListManager.all_lists)

def select_list(title_input):
    print("selecting list: some list")
    current_list = ListManager.all_lists[title_input]
    print(current_list.to_do_items)

# test commit
def main():
    print("called main")
    display_lists(ListManager.all_lists)
    query_list()
    query_list()

if __name__ == '__main__':
    main()