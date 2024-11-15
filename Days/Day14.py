import functions

todos = []
import time

while True:
    user_action = input(f"Enter add, show, edit, complete and your todo or enter exit. \n ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        try:
            todo = (user_action[4:] + "\n")

            todos = functions.get_todos()

            todos.append(todo)

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            index = index + 1
            print(f"{index} - {item}")


    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            nouveau_todo = input(f"Insert new todo \n")
            todos[number] = nouveau_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        remv = int(input(f"Number of the todo to complete : \n "))

        todos = functions.get_todos()

        remv = remv - 1
        todo_a_enlever = todos[remv].strip("\n")
        todos.pop(remv)

        functions.write_todos(todos)

        removed = f"Todo {todo_a_enlever} was completed!"

        print(removed)
        time.sleep(1.5)
        ques = input(f"Do you want to exit or continue? \n")
        match ques:
            case "exit":
                break
            case "continue":
                print("...")
                time.sleep(2)

    elif "exit" in user_action:
        break