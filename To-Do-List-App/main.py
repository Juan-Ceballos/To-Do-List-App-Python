from datetime import datetime
from list_manager import ListManager
import to_do_item
import to_do_list

def display_lists():
    main_list = ListManager.all_lists
    num_to_dos = len(main_list)
    if num_to_dos == 0:
        print("Empty")
    for num in range(num_to_dos):
        print(f"{num + 1} {main_list[num].title}")

def create_new_list():
    now = datetime.now()
    title_input = input("Please enter to do list title: ")
    new_list = to_do_list.ToDoList({}, title_input)
    new_list.to_do_items = add_to_dos()
    ListManager.all_lists.append(new_list)
    print("Displaying all to do lists")
    display_lists()

def display_to_dos(input_list):
    print(f"{input_list.title}:")
    print("------------------")
    for index, to_do in enumerate(input_list.to_do_items):
        print(f"{index + 1} {to_do.description}")
    print("------------------")
    print()

def add_to_do(input_list):
    print("test add to do")
    display_to_dos(input_list)

def del_to_do(input_list):
    display_to_dos(input_list)
    print("test delete list")

def select_list():
    select_query = input("Please select list number you want to select or type and enter [quit] to go back")
    if select_query.isdigit():
        selected_digit = int(select_query) - 1
        if selected_digit > len(ListManager.all_lists) or selected_digit < 0:
            print("List does not exist going back to main menu")
            display_lists()
        selected_list = ListManager.all_lists[int(select_query) - 1]
        print(f"{selected_list.title}:")
        print("------------------")
        for index,to_do in enumerate(selected_list.to_do_items):
            print(f"{index + 1} {to_do.description}")
        print("------------------")
        to_do_done = False
        while not to_do_done:
            print("Add to do press enter")
            print("to delete a to do type and enter [del]")
            print("quit to go back to main list")
            to_do_query = input()
            match to_do_query:
                case "":
                    add_to_do(selected_list)
                case "del":
                    del_to_do(selected_list)
                case "quit":
                    to_do_done = True
                    print("Back to main list")
                    display_lists()
    elif select_query == "quit":
        print("Back to main list")
        display_lists()
    else:
        print("Command or input not recognized going back to main menu")
        display_lists()

def delete_list():
    del_query = input("Please type and enter the number of the list to delete")
    if del_query.isdigit():
        del_num = int(del_query) - 1
        ListManager.all_lists.pop(del_num)
    else:
        print("do not recognize input going back to main list")
    display_lists()

def query_list():
    done = False
    while not done:
        selected_list = input("1) Press enter key to start a new list\n2) Type and enter [sel] to pick a list"
                              "\n3) Type and enter [del] to delete a list\n4) Type and enter [quit] to exit\n")
        match selected_list:
            case "quit":
                done = True
            case "":
                create_new_list()
            case "sel":
                select_list()
            case "del":
                delete_list()

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

def main():
    print("called main")
    display_lists()
    query_list()

if __name__ == '__main__':
    main()