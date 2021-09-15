# How am i going to store my data?
# list of todos

# can store info in a list

# MENU
# Press 1 to add task
# Press 2 to delete task (HARD MODE)
# Press 3 to view all tasks
# Press q to quit

# todos = {"high": [], "medium": [], "low": []}

# enter new todo
    # high, medium, low
# store todo item in list
    # high, medium, low
# display all of todos
# number items when displayed so user can delete items/upate items
    # allows user to select item for update/deletion
    # when user enters item --> item_num - 1 (to correlate to index)

# while loop to ask questions --> menu

import json

todos = {"high": [], "medium": [], "low": []}

# if app has already been used, uncomment this block:
with open('todo.json', 'r') as fh:
    todos = json.load(fh)

def print_todos():
    print("\nHere is your to-do list:\n")
    for key, val in todos.items():
        print(f"{key.upper()}:")
        index = 0
        for task in val:
            print(f"{index + 1}: {val[index]}")
            index += 1
        print("")

def invalid_input():
    print("\nYou did not choose a valid option. Please try again!\n")

print("\nWelcome to your to-do list app!\n")

app_running = True

while app_running == True:

    print("""
==== MENU ====
Please select from the following options:

- Press 1 to add task
- Press 2 to delete task
- Press 3 to view all tasks
- Press q to quit
""")

    choice = input("What would you like to do?: ")
    if choice == "1":
        new_item = input("What would you like to add?: ")
        priority = input("How important is this to you? 'High', 'Medium', 'Low'?: ").lower()
        if priority == 'high' or priority == 'medium' or priority == 'low':
            todos[priority].append(new_item)
            print(f"List updated! \"{todos[priority][-1]}\" added to list.")
        else:
            print("You did not choose a valid priority level. Please prioritize your life!")

    elif choice == "2":
        print_todos()
        which_priority = input("What priority level is your item?\n Enter one of the following: 'High', 'Medium', 'Low' ").lower()
        if which_priority == 'high' or which_priority == 'medium' or which_priority == 'low':
            item_to_del = int(input("\nWhat would you like to check off or delete? (Please enter a number): "))
            if item_to_del == 0:
                invalid_input()
            elif item_to_del > len(todos[which_priority]):
                invalid_input()
            elif item_to_del <= len(todos[which_priority]):
                print(f"\"{todos[which_priority][item_to_del - 1]}\" deleted!")
                del todos[which_priority][item_to_del - 1]
        else:
                invalid_input()

    elif choice == "3":
        print_todos()

    elif choice == "q":
        app_running = False
        print("\nGood luck with your day! Come back to check things off or add items!\n")

    else:
        invalid_input()
        
with open('todo.json', 'w') as fh:
    json.dump(todos, fh)