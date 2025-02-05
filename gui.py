from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='items',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['items'])
    match event:
        case "Add":
            items = functions.get_todos()
            new_todo = values['todo'] + "\n"
            items.append(new_todo)
            functions.write_todos(items)
            window['items'].update(values=items)
        case "Edit":
            todo_to_edit = values['items'][0]
            new_todo = values['todo']

            items = functions.get_todos()
            index = items.index(todo_to_edit)
            items[index] = new_todo
            functions.write_todos(items)
            window['items'].update(values=items)
        case "Complete":
            todo_to_complete = values['items'][0]
            items = functions.get_todos()
            items.remove(todo_to_complete)
            functions.write_todos(items)
            window['items'].update(values=items)
            window['todo'].update(value=' ')
        case "Exit":
            break
        case 'items':
            window['todo'].update(value=values['items'][0])
        case sg.WIN_CLOSED:
            break


window.close()
