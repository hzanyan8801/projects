#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    # match user_action:
    # case 'add':
    # if 'add' in user_action or 'new' in user_action:
    if user_action.startswith("add"):
        todo = user_action[4:]

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()
        # with open('todos.txt', 'r') as file:  <<replace with function
        # todos = file.readlines()

        todos.append(todo + '\n')

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        # with open('todos.txt', 'w') as file:
        # file.writelines(todos )
        functions.write_todos(todos)
    # case 'show':
    # elif 'show' in user_action:
    elif user_action.startswith("show"):
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()
        # with open('todos.txt', 'r') as file:
        # todos = file.readlines()
        # print(todos)
        # new_todos = [item.strip('\n') for item in todos]

        for index, items in enumerate(todos):
            items = items.title()
            items = items.strip('\n')
            row = f"{index + 1}-{items}"
            print(row)
    # case 'edit':
    # elif 'edit' in user_action:
    elif user_action.startswith("edit"):
        # number = int(input("Number of the todo to edit:"))
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            # with open('todos.txt', 'r') as file:
            # todos = file.readlines()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'

            # with open('todos.txt', 'w') as file:
            # todos = file.writelines(todos)
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
            # user_action = input("Type add, show, edit, complete or exit:")
            # user_action = user_action.strip()

    # case 'complete':
    # elif 'complete' in user_action:
    elif user_action.startswith("complete"):
        # number = int(input("Number of the todo to complete: "))
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            # with open('todos.txt', 'r') as file:
            # todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            # with open('todos.txt', 'w') as file:
            # todos = file.writelines(todos)
            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    # case 'exit':
    # elif 'exit' in user_action:
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, wrong input")

print("Bye!")
