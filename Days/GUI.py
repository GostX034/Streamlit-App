import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip= "Enter todo", key = "todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do list",
                   layout =[[label], [input_box, add_button]],
                   font=("Helvetica", 20))


while True :
    event, values = window.read()
    print(event)
    print(values)

