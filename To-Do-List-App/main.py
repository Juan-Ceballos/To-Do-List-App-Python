from datetime import datetime
import calendar
from list_manager import ListManager
from to_do_item import ToDoItem
from to_do_list import ToDoList


def display_lists():
    main_list = ListManager.all_lists
    num_to_dos = len(main_list)
    if num_to_dos == 0:
        print("Empty")
    for num in range(num_to_dos):
        print(f"{num + 1} {main_list[num].title}")

def create_new_list():
    now = datetime.now() # what am i doing with this
    title_input = input("Please enter to do list title: ")
    new_list = ToDoList({}, title_input)
    new_list.to_do_items = add_to_dos()
    ListManager.all_lists.append(new_list)
    print("Displaying all to do lists")
    display_lists()

# due date function
# takes inputs for the due date of a todo
# month/day/year
def valid_year(year):
    now = datetime.now()
    if year.isdigit():
        if int(year) >= now.year:
            return True
    return False

def valid_month(month):
    now = datetime.now()
    if month.isdigit():
        if int(month) >= now.month and int(month) > 0 and month < 13:
            return True
    return False

def valid_day(year, month, day):
    last_day = calendar.monthrange(year, month)[1]
    if day.isdigit():
        if day > 0 and last_day >= day >= month.day:
            return True
    return False

def query_year():
    year_query = input("Enter Year or type [quit]:\n")
    return year_query

def query_month():
    month_query = input("Enter Month or type [quit]:\n")
    return month_query

def query_day():
    day_query = input("Enter day or type [quit]:\n")
    return day_query

def query_due_date():
    year_to_check = query_year()
    while not valid_year(year_to_check):
        if year_to_check == "quit":
            return year_to_check
        year_to_check = query_year()
    month_to_check = query_month()
    while not valid_month(month_to_check):
        if month_to_check == "quit":
            return month_to_check
        month_to_check = query_month()
    day_to_check = query_day()
    while not valid_day(int(year_to_check), int(month_to_check), day_to_check):
        if day_to_check == "quit":
            return day_to_check
        day_to_check = query_day()

    if len(month_to_check) == 1:
        month_to_check = f"0{month_to_check}"
    if len(day_to_check) == 1:
        day_to_check = f"0{day_to_check}"

    return f"{month_to_check}/{day_to_check}/{year_to_check}"

# return list of todos or mutate list in class?
def query_to_dos():
    description_inquiry = input("Type and enter description of to-do or [quit]:\n")
    if description_inquiry == "quit":
        return
    due_date_inquiry = query_due_date()
    if due_date_inquiry == "quit":
        return
    return description_inquiry, due_date_inquiry

def add_to_dos_2(description, due_date):



def display_to_dos(input_list):
    print(f"{input_list.title}:")
    print("------------------")
    for index, to_do in enumerate(input_list.to_do_items):
        print(f"{index + 1} {to_do.description}")
    print("------------------")
    print()

def del_to_do(input_list):
    del_query = input("Type and enter the number to delete:\n")
    if del_query.isdigit():
        del_num = int(del_query) - 1
        input_list.to_do_items.pop(del_num)
        display_to_dos(input_list)
    else:
        print("do not recognize input going back to main list")
        display_lists()

def select_list():
    display_lists()
    select_query = input("* Please type number you want to select\n* To go back type and enter [quit]\n")
    if select_query.isdigit():
        selected_digit = int(select_query) - 1
        if selected_digit > len(ListManager.all_lists) or selected_digit < 0:
            print("List does not exist going back to main list")
            display_lists()
        selected_list = ListManager.all_lists[int(select_query) - 1]
        print(f"{selected_list.title}:")
        print("------------------")
        for index,to_do in enumerate(selected_list.to_do_items):
            print(f"{index + 1} {to_do.description}")
        print("------------------")
        to_do_done = False
        while not to_do_done:
            print("* Add to do press key [RETURN]")
            print("* to delete a to do type and enter [del]")
            print("* back to main list type and enter [quit]")
            to_do_query = input()
            match to_do_query:
                case "":
                    added_to_dos = add_to_dos()
                    selected_list.to_do_items = selected_list.to_do_items + added_to_dos
                    display_to_dos(selected_list)
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
        print("Command or input not recognized going back to main list")
        display_lists()

def delete_list():
    del_query = input("Type and enter the number you want to delete:\n")
    if del_query.isdigit():
        del_num = int(del_query) - 1
        ListManager.all_lists.pop(del_num)
    else:
        print("do not recognize input going back to main list")
    display_lists()

def query_list():
    done = False
    while not done:
        selected_list = input("* To start a new list press key [RETURN]\n* To view a list type and enter [sel]"
                              "\n* To delete a list type and enter [del]\n* To exit type and enter [quit]\n")
        match selected_list:
            case "quit":
                done = True
            case "":
                create_new_list()
            case "sel":
                select_list()
            case "del":
                delete_list()

def main():
    print("called main")
    query_due_date()
    display_lists()
    query_list()

if __name__ == '__main__':
    main()