# ------------------------------------------------------------------------------
# Name: Deepak Vadithala
# Course: MSc Data Science
# Submission Date: 03-Apr-2017
# ------------------------------------------------------------------------------

#  Loading all relevant TKinter modules instead of all the modules

from tkinter import Frame, Canvas, Menu, Entry, Listbox, Button, Label, StringVar
import numpy as np, math, os, csv

from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

from GUIconnection import GUIconnection
from Pt import Pt

from Distance import Distance
from nthPoint import nthPoint

my_output_to_save = []


class LineSimplification(Frame):
    def __init__(self, master=None):

        # ===========================================
        # Below functions marked between '=' signed commented are all
        # helper functions.
        # ===========================================
        # ------------------------------------------------------------------------------
        # Following three functions uses POLYMORPHISM and generates displayName, displayParameterName
        # and thinPoints based on the input (Plugins.txt or Listbox selection).
        #  Using Eval method to convert the string to object
        # ------------------------------------------------------------------------------
        def generate_plugin_names(input_file_name):
            output_list = []
            with open(input_file_name) as current_file:
                next(current_file)
                for each_line in current_file:
                    # Using displayName() method based on linesimplification algorithm selected
                    output_list.append(eval(each_line)().displayName())
            return output_list

        def generate_plugin_label(input_value):
            # Using displayParameterName() method based on linesimplification algorithm selected
            return eval(input_value)().displayParameterName()

        def generate_plugin_thinpoints(input_value, input_pts, input_param):
            # Using thinPoints method based on linesimplification algorithm selected
            return eval(input_value)().thinPoints(input_pts, input_param)

        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # This function loads the input data and returns a sorted numpy Array
        # ------------------------------------------------------------------------------
        def load_input_data(file_name):
            return np.genfromtxt(file_name, delimiter=',')

        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # This function sets the listbox's label based on the list item selection
        # ------------------------------------------------------------------------------
        def get_listbox_selection(listbox_event):
            my_widget = listbox_event.widget
            index = int(my_widget.curselection()[0])
            value = my_widget.get(index).rstrip('\r\n')
            my_dynamic_label_name.set(generate_plugin_label(value))

        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # This is a callback function which triggers the button click event
        # and it generates the MAP only when open menu selection is made.
        # ------------------------------------------------------------------------------
        def generate_open_map():
            try:
                with open('temp_file_name.txt', 'r') as my_file:
                    my_file_to_load = my_file.readline()
            except Exception:
                messagebox.showinfo("Alert!", "Please load a file")
                return None

            try:
                data = np.array(load_input_data(my_file_to_load))
            except Exception:
                messagebox.showinfo("Alert!", "Please select appropriate file")
                return None

            pt_data = []
            for i in range(len(data)):
                pt_data.append(Pt(float(data[i][1]), float(data[i][2])))

            my_long = []
            my_lat = []

            for j in range(len(pt_data)):
                my_long.append(pt_data[j].getX())
                my_lat.append(pt_data[j].getY())

            my_lat_min = min(my_lat)
            my_lat_max = max(my_lat)
            my_long_min = min(my_long)
            my_long_max = max(my_long)

            my_converted_list = []

            for my_index in range(0, len(my_lat)):
                my_converted_list.append((my_long[my_index] - my_long_min) * (400 / (my_long_max - my_long_min)) + 50)
                my_converted_list.append((400 - (my_lat[my_index] - my_lat_min) * (400 / (my_lat_max - my_lat_min))) + 50)

            canvas.delete("all")
            canvas.create_polygon(my_converted_list, outline="black", fill="red")

        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # This function gets triggered when file >> open menu is selected
        # ------------------------------------------------------------------------------
        def open_menu_file_loader():
            my_file = open('temp_file_name.txt', 'w')
            my_main_input_file = (askopenfilename().split('/')[-1])
            my_file.write(my_main_input_file)
            my_file.close()
            generate_open_map()
            return my_main_input_file

        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # This is a callback function which triggers the button click event
        # This function generates the map based on Pts and it scales
        #  to the canvas size. Also, this function stores the data for the
        # output file.
        # ------------------------------------------------------------------------------
        def generate_map_button_click():

            try:
                with open('temp_file_name.txt', 'r') as my_file:
                    my_file_to_load = my_file.readline()
            except Exception:
                messagebox.showinfo("Alert!", "Please load a file")
                return None

            try:
                data = np.array(load_input_data(my_file_to_load))
            except Exception:
                messagebox.showinfo("Alert!", "Please select appropriate file")
                return None

            try:
                my_current_list_selection = my_listbox.get(my_listbox.curselection()).rstrip('\r\n')
            except Exception:
                messagebox.showinfo("Alert!", "Please select a algorithm")
                return None

            try:
                my_input_entry_value = float(my_entry_box.get())
            except Exception:
                messagebox.showinfo("Alert!", "Please input correct value")
                return None

            pt_data = []
            for i in range(len(data)):
                pt_data.append(Pt(float(data[i][1]), float(data[i][2])))

            my_data = generate_plugin_thinpoints(my_listbox.get(my_listbox.curselection()), pt_data, my_input_entry_value)
            global my_output_to_save
            my_output_to_save = []
            for my_line_index in range(len(my_data)):
                my_output_to_save.append((str(my_line_index + 1).rstrip('\n\r'), my_data[my_line_index].getX(), my_data[my_line_index].getY()))

            my_long = []
            my_lat = []

            for j in range(len(my_data)):
                my_long.append(my_data[j].getX())
                my_lat.append(my_data[j].getY())

            my_lat_min = min(my_lat)
            my_lat_max = max(my_lat)
            my_long_min = min(my_long)
            my_long_max = max(my_long)

            my_converted_list = []

            for my_index in range(0, len(my_lat)):
                try:
                    ((my_long[my_index] - my_long_min) * (400 / (my_long_max - my_long_min)) + 50) or (
                    (400 - (my_lat[my_index] - my_lat_min) * (400 / (my_lat_max - my_lat_min))) + 50)
                except ZeroDivisionError:
                    messagebox.showinfo("Alert!", "Value entered out of possible range!!")
                    return None

                my_converted_list.append((my_long[my_index] - my_long_min) * (400 / (my_long_max - my_long_min)) + 50)
                my_converted_list.append((400 - (my_lat[my_index] - my_lat_min) * (400 / (my_lat_max - my_lat_min))) + 50)

            canvas.delete("all")
            canvas.create_polygon(my_converted_list, outline="black", fill="red")

        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # This is a callback function which saves the output and stores
        #  the data in CSV format. Please use the extension CSV.
        # ------------------------------------------------------------------------------
        def file_save():
            # print(my_output_to_save)
            filename = asksaveasfilename(title="Please select data file to save")
            if len(filename) > 0:
                with open(filename, 'w') as out:
                    csv_out = csv.writer(out)
                    for i in range(len(my_output_to_save)):
                        csv_out.writerow(my_output_to_save[i])
        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        # This function will close the window
        # ------------------------------------------------------------------------------
        def close_window():
            self.master.destroy()
        # ------------------------------------------------------------------------------
        # ===========================================

        # ------------------------------------------------------------------------------
        # This section of the code generate the GUI
        # ------------------------------------------------------------------------------
        Frame.__init__(self, master)

        my_menubar = Menu(self.master)
        my_file_menu = Menu(my_menubar, tearoff=0)
        my_file_menu.add_command(label="Open", command=open_menu_file_loader)
        my_file_menu.add_command(label="Save", command=file_save)
        my_file_menu.add_command(label="Close", command=close_window)

        my_file_menu.add_command(label="Exit", command=self.master.quit)
        my_menubar.add_cascade(label="File", menu=my_file_menu)
        self.master.config(menu=my_menubar)

        canvas = Canvas(self.master, width=500, height=500)
        self.grid(row=0, column=4)
        self.grid(row=1, column=1, columnspan=5)
        my_button = Button(text="Process", command=generate_map_button_click)

        my_dynamic_label_name = StringVar()
        my_dynamic_label_name.set('Select a list item')
        my_label_01 = Label(text="Select Method")
        my_label_02 = Label(textvariable=my_dynamic_label_name, width=13)
        my_entry_box = Entry(bd=1, width=6)

        my_listbox_items = generate_plugin_names('plugins.txt')
        my_listbox = Listbox(self.master, height=len(my_listbox_items) + 1)

        my_list_value = 1
        for list_item in my_listbox_items:
            my_listbox.insert(my_list_value, list_item)
            my_list_value  =  my_list_value + 1

        my_listbox.bind('<<ListboxSelect>>', get_listbox_selection)

        my_label_01.grid(row=0, column=0)
        my_listbox.grid(row=0, column=1, padx=10)
        my_label_02.grid(row=0, column=2, padx=5)
        self.grid_columnconfigure(2, minsize=125)
        my_entry_box.grid(row=0, column=3)
        my_button.grid(row=0, column=4)

        my_button.grid(row=0, column=4)
        canvas.grid(row=1, column=1, columnspan=5)

        self.master.title("Line Simplification")


if __name__ == "__main__":
    LineSimplification().mainloop()

# ------------------------------------------------------------------------------
# This code cleans up temp file
# ------------------------------------------------------------------------------
try:
    os.remove('temp_file_name.txt')
except OSError:
    pass
