FILEPATH = "todos.txt"


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file :
        file.writelines(todos_arg)

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

if __name__ == "__main__" :
    print("Bonjour!")