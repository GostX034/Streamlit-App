todos = []
import time
while True :
    user_action = input(f"Do you want to add, show, edit, complete or exit your todos ? \n ")
    user_action = user_action.strip()

    match user_action :
        case "add" :
            todo = input(f"Enter a todo \n ") + "\n"

            with open("todos.txt", "r") as file :
                file.readlines()


            todos.append(todo)

            with open("todos.txt", "w") as file :
                file.writelines(todos)

        case "show" :
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for  index, item in enumerate(todos):
                index = index + 1
                print(f"{index} - {item}")
        case "edit" :
            number = int(input(f"Enter number of the todo \n "))
            number = number - 1
            with open("todos.txt", "r") as file :
                file.readlines()

            nouveau_todo = input(f"Insert new todo \n")
            todos[number] = nouveau_todo + '\n'

            with open("todos.txt", "w") as file :
                file.writelines(todos)
        case "complete" :
            remv = int(input(f"Number of the todo to complete : \n "))

            with open("todos.txt", "r") as file :
                file.readlines()
            remv = remv - 1
            todo_a_enlever = todos[remv].strip("\n")
            todos.pop(remv)
            with open("todos.txt", "w") as file :
                file.writelines(todos)
            removed = f"Todo {todo_a_enlever} was completed!"
            print(removed)
            time.sleep(1.5)
            ques = input(f"Do you want to exit or continue? \n")
            match ques :
                case "exit" :
                    break
                case "continue" :
                    print("...")
                    time.sleep(2)
        case "exit":
            break