
todos = ["pet the cat", "go to work", "shop for groceries", 
"go home", "feed the cat"]

todos += ["binge watch a show", "go to sleep"]
todos.extend(["binge watch a show", "go to sleep"])

index = 0

# # while index < len(todos):
#     print(f"{index + 1}: {todos[index]}")
#     index += 1

# Let's modify our to-do program



# prompting the user for items to add.
new_item = input("Add an item? Type it here: ")

while len(new_item) > 0: # If the user just presses Enter, the program will exit.
    todos.append(new_item) # If they do provide a new to-do, we'll add it 
    # to the list and print their current to-do items.
    print(todos) # Print list every time user inserts a new todo list item
    new_item = input("Add an item? Type it here: ")
print(f"Okay, here is your list: {todos}") # Print list once has terminated the program