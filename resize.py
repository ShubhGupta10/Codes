# Import module 
from tkinter import *

# Create object 
root = Tk()

# Adjust size 
root.geometry("400x400")

# Specify Grid
Grid.columnconfigure(root, index = 0,
					weight = 1)

Grid.rowconfigure(root, 0, 
				weight = 1)

# Create Buttons
button_1 = Button(root, text = "Button 1",height=2,width=10,bg="red")

# Set grid
button_1.grid(row = 0,
			column = 0, sticky = "NSEW")

# resize button text size
def resize(e):
	
	# get window width  
	size = e.width/10

	# define text size on different condition

	# if window height is greater 
	# than 300 and less than 400 (set font size 40)
	if e.height <= 400 and e.height > 300:
		button_1.config(font = ("Helvetica", 40))

	# if window height is greater than 
	# 200 and less than 300 (set font size 30)
	elif e.height < 300 and e.height > 200:
		button_1.config(font = ("Helvetica", 30))

	# if window height is less
	# than 200 (set font size 40)
	elif e.height < 200:
		button_1.config(font = ("Helvetica", 40))

# it will call resize function 
# when window size will change
root.bind('<Configure>', resize)

# Execute tkinter
root.mainloop()
