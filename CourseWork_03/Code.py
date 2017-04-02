import math, numpy as np,random as rand
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
np.set_printoptions(precision=15)

root = Tk()
canvas = Canvas(root, width=500, height=500)

# ------------------------------------------------------------------------------
# Function to calculate the nth Plot algorithm
# ------------------------------------------------------------------------------
def nthPlot(data,n):
    count = 0
    newdata = []
    for i in range(len(data)):
        if i % n == 0:
            count = count + 1
            temp = [count, float(data[i][1]), float(data[i][2])]
            newdata.append(temp)
    return newdata
#------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Function to calculate the Distance algorithm
#------------------------------------------------------------------------------
def Distance(data, mindist):
    count = 1
    newdata = []
    lastKept = float(data[0][1]), float(data[0][2])
    temp = [count, float(data[0][1]), float(data[0][2])]
    newdata.append(temp)
    for i in range(1, len(data)):
        current = float(data[i][1]), float(data[i][2])
        if EucledeanDistance(lastKept, current) >= mindist:
            count = count + 1
            temp = [count, float(data[i][1]), float(data[i][2])]
            lastKept = float(data[i][1]), float(data[i][2])
            newdata.append(temp)
    return newdata
#------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Function to calculate the EucledeanDistance algorithm
#------------------------------------------------------------------------------
def EucledeanDistance(lastKept, current):
    return math.sqrt(math.pow((current[0] - lastKept[0]), 2) + math.pow((current[1] - lastKept[1]), 2))
#------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# This functions reads the plugins.txt file and lists all the algorithms available
#------------------------------------------------------------------------------
def generate_algorithm_plugins(input_file_name):
    output_list = []
    with open(input_file_name) as current_file:
        next(current_file)
        for each_line in current_file:
            output_list.append(each_line)
    return output_list
#------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# This function loads the input data and retuns a numpy Array
#------------------------------------------------------------------------------
def load_input_data(file_name):
    return np.genfromtxt(file_name, delimiter=',')
#------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Test function to make sure file menu events are triggers. To be replaced!
#------------------------------------------------------------------------------
def open_menu_file_loader():
    my_file = open('temp_file_name.txt', 'w')
    # print('test')
    my_main_input_file = (askopenfilename().split('/')[-1])
    my_file.write(my_main_input_file)
    my_file.close()
    generate_open_map()
    return my_main_input_file
#------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# This function generates the label text based on the list item selected
#------------------------------------------------------------------------------
def get_label_text(my_selected_listbox_value):
    # print(my_selected_listbox_value)
    if my_selected_listbox_value == 'Distance':
        my_dynamic_label_name.set('min distance')
    elif my_selected_listbox_value == 'nthPoint':
        my_dynamic_label_name.set('n = ')
    else:
        my_dynamic_label_name.set('Select a list item')
#------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# This function captures the list item selection change event
#------------------------------------------------------------------------------
def get_listbox_selection(listbox_event):
    my_widget = listbox_event.widget
    index = int(my_widget.curselection()[0])
    value = my_widget.get(index).rstrip('\r\n')
    get_label_text(value)
    my_entry_box.delete(0, END)
    # print(value)
    return value
#------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# This is a callback function which triggers the button click event
#------------------------------------------------------------------------------
def generate_open_map():
    with open('temp_file_name.txt', 'r') as my_file:
        my_file_to_load = my_file.readline()

    my_data = np.array(load_input_data(my_file_to_load))
     
    my_long = list(my_data[:, 1])
    my_lat = list(my_data[:, 2])

    my_lat_min = min(my_lat)
    my_lat_max = max(my_lat)
    my_long_min = min(my_long)
    my_long_max = max(my_long)

    # print(my_lat, my_long)
    my_converted_list = []

    for my_index in range(0, len(my_lat)):
        my_converted_list.append((my_long[my_index] - my_long_min) * (400 / (my_long_max - my_long_min)) + 50)
        my_converted_list.append((400 - (my_lat[my_index] - my_lat_min) * (400 / (my_lat_max - my_lat_min))) + 50)

    # canvas.create_polygon([50, 150, 150, 50, 250, 150, 150, 250],   outline ="black", fill = "green")
    canvas.delete("all")
    canvas.create_polygon(my_converted_list, outline ="black", fill = "red")
#------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# This is a callback function which triggers the button click event
#------------------------------------------------------------------------------
def generate_map_button_click():

    with open('temp_file_name.txt', 'r') as my_file:
        my_file_to_load = my_file.readline()

    # print(my_file_to_load)
    try:
        my_current_list_selection =  my_listbox.get(my_listbox.curselection()).rstrip('\r\n')
    except Exception as e:
       messagebox.showinfo("Alert!", "Please select a algorithm")
       return None

    my_input_box_value = float(my_entry_box.get())

    if my_current_list_selection == 'Distance':       
        my_data = np.array(Distance(load_input_data(my_file_to_load), my_input_box_value))
        # print(len(my_data))
        # print(my_data[:10])
    elif my_current_list_selection == 'nthPoint':
        my_data = np.array(nthPlot(load_input_data(my_file_to_load), my_input_box_value))
        # print(len(my_data))
        # print(my_data[:10])
    else:
        my_data = np.array(nthPlot(load_input_data(my_file_to_load), my_input_box_value))
     

    my_long = list(my_data[:, 1])
    my_lat = list(my_data[:, 2])

    my_lat_min = min(my_lat)
    my_lat_max = max(my_lat)
    my_long_min = min(my_long)
    my_long_max = max(my_long)

    my_converted_list = []

    for my_index in range(0, len(my_lat)):
        my_converted_list.append((my_long[my_index] - my_long_min) * (400 / (my_long_max - my_long_min)) + 50)
        my_converted_list.append((400 - (my_lat[my_index] - my_lat_min) * (400 / (my_lat_max - my_lat_min))) + 50)

    # canvas.create_polygon([50, 150, 150, 50, 250, 150, 150, 250],   outline ="black", fill = "green")
    canvas.delete("all")
    canvas.create_polygon(my_converted_list, outline ="black", fill = "red")
#------------------------------------------------------------------------------


my_frame = Frame(root)
my_frame.grid()

my_menubar = Menu(root)
my_file_menu = Menu(my_menubar, tearoff=0)
my_file_menu.add_command(label="Open", command=open_menu_file_loader)
my_file_menu.add_command(label="Save", command=open_menu_file_loader)
my_file_menu.add_command(label="Close", command=open_menu_file_loader)

my_file_menu.add_command(label="Exit", command=root.quit)
my_menubar.add_cascade(label="File", menu=my_file_menu)
root.config(menu=my_menubar)

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


my_listbox.bind('<<ListboxSelect>>', get_listbox_selection)

my_label_01.grid(row = 0, column = 0)
my_listbox.grid(row = 0,column = 1, padx=10)
my_label_02.grid(row=0, column=2, padx=5, sticky=E)
root.grid_columnconfigure(2, minsize=125)
my_entry_box.grid(row = 0, column = 3)
my_button.grid(row=0, column = 4)
canvas.grid(row = 1, column = 1, columnspan = 5)

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
