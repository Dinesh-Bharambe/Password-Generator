import random
import pyperclip
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window = Tk()
window.geometry("450x120")

window.title("Password Generator")

def low():
	entry.delete(0, END)
	length = var1.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = ""
	
	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password
	
	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(upper)
		return password
	
	elif var.get() == 3:
		for i in range(0, length):
			password = password + random.choice(digits)
		return password
	else:
		print("Please choose an option")

def generate():
	password1 = low()
	entry.insert(10, password1)

def copy():
	random_password = entry.get()
	pyperclip.copy(random_password)
	messagebox.showinfo("Successful","Password copied in clipboard! ")

Random_password = Label(window, text="Password")
Random_password.grid(row=0)
entry = Entry(window)
entry.grid(row=0, column=1)

c_label = Label(window, text="Length")
c_label.grid(row=1)

copy_button = Button(window, text="Copy", command=copy)
copy_button.grid(row=0, column=2)
generate_button = Button(window, text="Generate", command=generate)
generate_button.grid(row=0, column=3)

var = IntVar()
radio_low = Radiobutton(window, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')

radio_middle = Radiobutton(window, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')

radio_strong = Radiobutton(window, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')

var1 = IntVar()
combo = Combobox(window, textvariable=var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
		   17, 18, 19, 20, 21, 22, 23, 24, 25,
		   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

window.mainloop()
