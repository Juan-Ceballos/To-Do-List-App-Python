from datetime import datetime
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
        print("picked a list")
    else:
        create_new_list()



# def add_to_dos(curr_list):
#     description_inquiry = input("Please add to do description or enter /f to finish: ")
#     if description_inquiry != "/f":
#
#         curr_to_do = to_do_item.ToDoItem()
#         curr_list.add_to_do()



def create_new_list():
    title_input = input("Please enter to do list title: ")
    now = datetime.now()
    new_list = to_do_list.ToDoList({}, title_input)
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