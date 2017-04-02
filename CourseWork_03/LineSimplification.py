from tkinter import Frame, Canvas, Menu, Entry, Listbox, Button, Label, StringVar
import numpy as np, math

from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

from GUIconnection import GUIconnection
from Pt import Pt


from Distance import Distance
from nthPoint import nthPoint

class LineSimplification(Frame):

	def __init__(self, master = None):


		# ------------------------------------------------------------------------------
		# This functions reads the plugins.txt file and lists all the algorithms available
		#------------------------------------------------------------------------------
		def generate_plugin_names(input_file_name):
			output_list = []
			with open(input_file_name) as current_file:
				next(current_file)
				for each_line in current_file:
					output_list.append(eval(each_line)().displayName())
			return output_list

		def generate_plugin_label(input_value):
			return eval(input_value)().displayParameterName()

		def generate_plugin_thinpoints(input_value, input_pts, input_param):
			return eval(input_value)().thinPoints(input_pts, input_param)		
		#------------------------------------------------------------------------------


		#------------------------------------------------------------------------------
		# This function loads the input data and retuns a numpy Array
		#------------------------------------------------------------------------------
		def load_input_data(file_name):
		    return np.genfromtxt(file_name, delimiter=',')
		#------------------------------------------------------------------------------


		# ------------------------------------------------------------------------------
		# This function captures the list item selection change event
		#------------------------------------------------------------------------------
		def get_listbox_selection(listbox_event):
		    my_widget = listbox_event.widget
		    index = int(my_widget.curselection()[0])
		    value = my_widget.get(index).rstrip('\r\n')
		    my_dynamic_label_name.set(generate_plugin_label(value))
		    # my_entry_box.delete(0, END)
		    # print(value)
		    return value
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
		    except Exception:
		       messagebox.showinfo("Alert!", "Please select a algorithm")
		       return None

		    try:
		        my_input_entry_value = float(my_entry_box.get())
		    except Exception:
		       messagebox.showinfo("Alert!", "Please input correct value")
		       return None

		    data = load_input_data("MainlandUKoutline.csv")

		    pt_data = []
		    for i in range(len(data)):
		    	pt_data.append(Pt(float(data[i][1]), float(data[i][2])))

		    my_data = generate_plugin_thinpoints(my_listbox.get(my_listbox.curselection()), pt_data, my_input_entry_value)

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
		    		((my_long[my_index] - my_long_min) * (400 / (my_long_max - my_long_min)) + 50) or ((400 - (my_lat[my_index] - my_lat_min) * (400 / (my_lat_max - my_lat_min))) + 50)
		    	except ZeroDivisionError:
		    		messagebox.showinfo("Alert!", "Value entered out of possible range!!")
		    		return None

		    	my_converted_list.append((my_long[my_index] - my_long_min) * (400 / (my_long_max - my_long_min)) + 50)
		    	my_converted_list.append((400 - (my_lat[my_index] - my_lat_min) * (400 / (my_lat_max - my_lat_min))) + 50)

		    # canvas.create_polygon([50, 150, 150, 50, 250, 150, 150, 250],   outline ="black", fill = "green")
		    canvas.delete("all")
		    canvas.create_polygon(my_converted_list, outline ="black", fill = "red")
		#------------------------------------------------------------------------------

		my_class_instance = nthPoint()
		my_input_data = load_input_data('MainlandUKOutline.csv')

		my_output_list  = my_class_instance.thinPoints(my_input_data, 1000)
		print(len(my_output_list))


		Frame.__init__(self, master)
		# self.grid()


		canvas = Canvas(self.master, width=500, height=500)
		self.grid(row=0, column = 4)
		self.grid(row = 1, column = 1, columnspan = 5)
		my_button = Button(text = "Process", command = generate_map_button_click)

		my_dynamic_label_name = StringVar()
		my_dynamic_label_name.set('Select a list item')
		my_label_01 = Label(text="Select Method")
		my_label_02 = Label(textvariable=my_dynamic_label_name)
		my_entry_box = Entry(bd=1, width = 6)

		my_listbox_items = generate_plugin_names('plugins.txt')
		my_listbox = Listbox(self.master, height=len(my_listbox_items) + 1)

		my_list_value = 1
		for list_item in my_listbox_items:
		    my_listbox.insert(my_list_value, list_item)
		    my_list_value = my_list_value + 1

		my_listbox.bind('<<ListboxSelect>>', get_listbox_selection)    

		my_label_01.grid(row = 0, column = 0)
		my_listbox.grid(row = 0,column = 1, padx=10)
		my_label_02.grid(row=0, column=2, padx=5)
		self.grid_columnconfigure(2, minsize=125)
		my_entry_box.grid(row = 0, column = 3)
		my_button.grid(row=0, column = 4)		

		my_button.grid(row=0, column = 4)
		canvas.grid(row = 1, column = 1, columnspan = 5)

		self.master.title("Line Simplification")


if __name__ == "__main__":
	LineSimplification().mainloop()
