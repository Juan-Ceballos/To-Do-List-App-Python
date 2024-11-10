from datetime import datetime

import list_manager
import to_do_item
from list_manager import ListManager
import to_do_list
from to_do_item import ToDoItem
from to_do_list import ToDoList


def display_lists(lists):
    num_to_dos = len(lists)
    if num_to_dos == 0:
        print("Empty")
    for num in range(num_to_dos):
        print(f"{num + 1} {lists[num].title}")

def query_list():
    selected_list = input("Select list by number or enter anything to start a new to do list: ")
    if selected_list.isdigit():
        all_list_count = ListManager.all_lists.count()
        if selected_list > all_list_count:
            print("List does not exist")
            query_list()
    else:
        create_new_list()



def add_to_dos():
    to_do_inputs = []
    done = False
    while not done:
        description_inquiry = input("Enter to do if done enter DONE: ")
        if description_inquiry != "DONE":
            curr_to_do = to_do_item.ToDoItem(description_inquiry)
            to_do_inputs.append(curr_to_do)
        else:
            done = True
    return to_do_inputs



def create_new_list():
    now = datetime.now()
    title_input = input("Please enter to do list title: ")
    # fill list of todos here first?
    new_list = to_do_list.ToDoList({}, title_input)
    new_list.to_do_items = add_to_dos()
    ListManager.all_lists.append(new_list)
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
    #query_list()

if __name__ == '__main__':
    main()