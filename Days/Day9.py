todos = []
import time
while True :
    user_action = input(f"Enter add, show, edit, complete and your todo or enter exit. \n ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = (user_action[4:] + "\n")

        with open("todos.txt", "r") as file :
            file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file :
            file.writelines(todos)


    elif user_action.startswith("show"):
        with open("todos.txt" , "r") as file :
            todos = file.readlines()

        for  index, item in enumerate(todos):
            index = index + 1
            print(f"{index} - {item}")


    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        number = number - 1

        with open("todos.txt", "r") as file :
           todos =  file.readlines()


        nouveau_todo = input(f"Insert new todo \n")
        todos[number] = nouveau_todo + '\n'

        with open("todos.txt", "w") as file :
            file.writelines(todos)



    elif user_action.startswith("complete"):
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


    elif "exit" in user_action :
        break

    else :
        print(f"Silly you, command is not valid ! Try again. \n")
        time.sleep(2)
        continue


bye_message = f"Bye bye! Hope you have a great day \n "
print(bye_message)