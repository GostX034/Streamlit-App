import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()

def add_todo():
    todo = st.session_state["nouveau_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)

st.title("Mon Application De Liste ")
st.write("Ceci est un PP de Thomas Gaudreault")

for todo in todos:
   st.checkbox(todo)

st.text_input(label = "" , placeholder = "Ajouter un point: ",
              on_change = add_todo , key = "nouveau_todo")











