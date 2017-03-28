import numpy as np,random as rand
from tkinter import *
root = Tk()
canvas = Canvas(root, width = 500, height = 500)

def generate_algorithm_plugins(input_file_name):
    output_list = []
    with open(input_file_name) as current_file:
        next(current_file)
        for each_line in current_file:
            output_list.append(each_line)
    return output_list

def load_input_data(file_name):
    return np.genfromtxt(file_name, delimiter= ',')


def generate_map_button_click():
    my_UK_data = load_input_data('MainlandUKoutline.csv')

    my_long = list(my_UK_data[:, 1])
    my_lat = list(my_UK_data[:, 2])

    my_lat_min = min(my_lat)
    my_lat_max = max(my_lat)
    my_long_min = min(my_long)
    my_long_max = max(my_long)
    my_converted_list = []

    for my_index in range(0, len(my_lat)):
        my_converted_list.append((my_long[my_index] - my_long_min) * (400 / (my_long_max - my_long_min)) + 50)
        my_converted_list.append((400 - (my_lat[my_index] - my_lat_min) * (400 / (my_lat_max - my_lat_min))) + 50)

    # canvas.create_polygon([50, 150, 150, 50, 250, 150, 150, 250],   outline ="black", fill = "green")
    canvas.create_polygon(my_converted_list, outline ="black", fill = "red")

def open_menu_file_loader():
    print('test')

my_frame = Frame(root)
my_frame.grid()

my_menu = Menu(root)
my_file_menu = Menu(my_menu, tearoff= 0)
my_file_menu.add_command(label = "Open", command = open_menu_file_loader)
my_file_menu.add_command(label = "Save", command = open_menu_file_loader)
root.config(menu = my_menu)


my_dynamic_label_name = StringVar()
my_dynamic_label_name.set('Select a list item')
my_label_01 = Label(text="Select Method")
my_label_02 = Label( textvariable=my_dynamic_label_name)
my_entry_box = Entry(bd=1, width = 6)


my_listbox_items = generate_algorithm_plugins('plugins.txt')
my_listbox = Listbox(root, height=len(my_listbox_items) + 1)

my_button = Button(text = "Process", command = generate_map_button_click)

my_list_value = 1
for list_item in my_listbox_items:
    my_listbox.insert(my_list_value, list_item)
    my_list_value = my_list_value + 1




def get_label_text(my_selected_listbox_value):
    # print(my_selected_listbox_value)
    if my_selected_listbox_value == 'Distance':
        my_dynamic_label_name.set('min distance')
    elif my_selected_listbox_value == 'nthPoint':
        my_dynamic_label_name.set('n = ')
    else:
        my_dynamic_label_name.set('Select a list item')


def get_listbox_selection(listbox_event):
    my_widget = listbox_event.widget
    index = int(my_widget.curselection()[0])
    value = my_widget.get(index).rstrip('\r\n')
    get_label_text(value)
    # print(value)
    return value

my_listbox.bind('<<ListboxSelect>>', get_listbox_selection)

my_label_01.grid(row = 0, column = 0)
my_listbox.grid(row = 0,column = 1, padx=10)
my_label_02.grid(row = 0, column = 2, padx=10)
my_entry_box.grid(row = 0, column = 3)
my_button.grid(row=0, column = 4)
canvas.grid(row = 1, column = 1, columnspan = 5)


# canvas.create_rectangle( 25, 25, 375, 375, fill="purple", width=0)
root.mainloop()



# Use inheritence and allow users to import new simplification algorithm
# Use the point class to store the data. Someone might load the Z value
# Scaling should be to display the map but don't change the data
# Read the plugins.txt to get list of algorithms
# Use GUIconnection.py file classes. Don't add any new class and use the existing class.
# Make sure error handling is coded when something correct is not typed
# 400 - x or 400 - y
# Lock the window size
# Main file is linesimplificationq

# mbar and file menu



# print(generate_algorithm_plugins('plugins.txt'))
