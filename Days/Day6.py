todos = []
import time
while True :
    user_action = input("Do you want to add, show, edit, complete or exit your todos ?")
    user_action = user_action.strip()

    match user_action :
        case "add" :
            todo = input("Enter a todo") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show" :
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for  index, item in enumerate(todos):
                index = index + 1
                print(f"{index} - {item}")
        case "edit" :
            number = int(input("Enter number of the todo"))
            number = number - 1
            nouveau_todo = input("Insert new todo")
            todos[number] = nouveau_todo
        case "complete" :
            remv = int(input("Number of the todo to complete :"))
            remv = remv - 1
            todos.pop(remv)
            print("Todo completed!")
            time.sleep(1.5)
            ques = input("Do you want to exit or continue?")
            match ques :
                case "exit" :
                    break
                case "continue" :
                    print("...")
                    time.sleep(2)
        case "exit":
            break