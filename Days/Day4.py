todos = []

while True :
    user_action = input("Type add, show, edit,or exit")
    user_action = user_action.strip()

    match user_action :
        case "add" :
            todo = input("Enter a todo")
            todos.append(todo)
        case "show" :
            for   item in todos:
                print(item)
        case ("edit") :
            number = int(input("Enter number of the todo"))
            number = number - 1
            nouveau_todo = input("Insert new todo")
            todos[number] = nouveau_todo
        case "exit":
            break