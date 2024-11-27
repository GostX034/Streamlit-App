FILEPATH = "todos.txt"
import streamlit as st
"""Reecrit la liste a faire dans le document .txt ."""
def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file :
        file.writelines(todos_arg)

"""Receuille la liste du document .txt a l'ouverture du programme."""
def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

"""Ajoute un point dans la version web-app"""
#def add_todo():
   # todo = st.session_state["nouveau_todo"]
   # todos.append(todo)
   # write_todos(todos)


"""Complete un point dans la version web app """


