# from tkinter import *
# from tkinter import ttk
# import tkinter
#
#
# def selection():
#     try:
#         # print(Lb1.get(Lb1.curselection()))
#         for i in Lb1.curselection():
#             print(Lb1.get(i))
#     except Lb1.get(Lb1.curselection(), last=None) == NONE:
#         print("Veuillez selectionner au moins une valeur")
#
#
# def start():
#     Lb1.delete(0, 5)
#     Lb1.pack()
#
#
# def insertion(element):
#     # print(Lb1.insert(END, element))
#     print(element)
#
#
# def recupVal():
#     print(entry_field.get())
#
#
# root = Tk()
#
# Lb1 = Listbox(root, selectmode=MULTIPLE)
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Perl")
# Lb1.insert(3, "C")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JSP")
# Lb1.insert(6, "Ruby")
#
# Lb1.pack()
#
# quit_button = ttk.Button(text="Quit", command=root.destroy).pack()
# valid_button = ttk.Button(text="Validate", command=selection).pack()
#
# start_button = ttk.Button(text="Start", command=start).pack()
#
# button = Button(root, text="Valider", command=recupVal).pack()
#
# label_field = Label(root, text="add a word").pack(side=LEFT)
#
# entry_field = Entry(root, bd=5)
# entry_field.pack(side=RIGHT)
#
# root.mainloop()


# --------------------------------------------------------------------------------------------------------------
import tkinter
from tkinter import *
import tkinter as tk

# Create a window object
window = tk.Tk()


# label = tk.Label(
#     text="Hello, Tkinter",
#     fg="white",
#     bg="black",
#     width=10,
#     height=10).pack()
#
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow"
# ).pack()
# window.mainloop()
# --------------------

# def add_name():
#     name = entry.get()
#     print(name)
#
#
# def delete_name():
#     entry.delete(0, tk.END)
#
#
# def insert_name():
#     entry.insert(0, "Python")
#     entry.insert(0, "Real ")
#
#
# label = tk.Label(window, text="Name")
# entry = tk.Entry(window)
# button_Name = tk.Button(window, text="Validate", command=add_name)
# button_Delete = tk.Button(window, text="Delete", command=delete_name)
# button_Insert = tk.Button(window, text="Insert", command=insert_name)
# label.pack()
# entry.pack()
# button_Name.pack(side=LEFT)
# button_Delete.pack(side=LEFT)
# button_Insert.pack(side=LEFT)

# window.mainloop()


# --------------------

# def Get():
#     print(text_box.get("1.0", tk.END))
#
#
# def Delete_charactere():
#     text_box.delete("1.0")
#
#
# def Delete_All():
#     text_box.delete("1.0", tk.END)
#
#
# def Insert():
#     text_box.insert("1.0", "Hello")
#
#
# def Insert2():
#     text_box.insert("2.0", " world!")
#
#
# def InsertAtTheEnd():
#     text_box.insert(tk.END, "\nPut me on at the end!")
#
#
# text_box = tk.Text(window)
# button_Delete_Charactere = tk.Button(window, text="Delete Char", height=1, width=12,  command=Delete_charactere)
# button_Delete_All = tk.Button(window, text="Delete All", height=1, width=12,  command=Delete_All)
# button_Insert = tk.Button(window, text="Insert", height=1, width=12,  command=Insert)
# button_Insert2 = tk.Button(window, text="Insert 2", height=1, width=12,  command=Insert2)
# button_InsertAtTheEnd = tk.Button(window, text="Insert at the end", height=1, width=12,  command=InsertAtTheEnd)
# button_Get = tk.Button(window, text="Get", height=1, width=12, command=Get)
# text_box.pack(side=RIGHT)
# button_Insert.pack(side=TOP)
# button_Insert2.pack(side=TOP)
# button_InsertAtTheEnd.pack(side=TOP)
# button_Delete_Charactere.pack(side=TOP)
# button_Delete_All.pack(side=TOP)
# button_Get.pack(side=TOP)
#
# window.mainloop()

# --------------------
# frame_a = tk.Frame()
# frame_b = tk.Frame()
#
#
# label_a = tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()
#
# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()
#
# frame_a.pack()
# frame_b.pack()
#
# window.mainloop()

# --------------------

# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }
#
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()

# window.mainloop()

# --------------------

# # Exercice: Write a complete script that displays an Entry widget that’s 40 text units wide and has a white background
# # and black text. Use .insert() to display text in the widget that reads "What is your name?".
# entry = tk.Entry(window, width=40, bg="white", fg="black")
# entry.pack()
#
# entry.insert(0, "What is your name")
#
# window.mainloop()

# --------------------

# Controlling Layout with Geometry Managers
# The .pack() Geometry Manager

# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# window.mainloop()

# --------------------

# # The .place() Geometry Manager
# frame = tk.Frame(master=window, width=150, height=150)
# frame.pack()
#
# label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
# label1.place(x=0, y=0)
#
# label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
# label2.place(x=75, y=75)
#
# window.mainloop()

# --------------------

# The .grid() Geometry Manager

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)
#     for j in range(3):
#         frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()

# --------------------


# window.columnconfigure(0, minsize=250)
# window.rowconfigure([0, 1], minsize=100)
#
# label1 = tk.Label(text="A")
# label1.grid(row=0, column=0, sticky="n")
#
# label2 = tk.Label(text="B")
# label2.grid(row=1, column=0, sticky="n")
#
# window.mainloop()

# --------------------

# window.rowconfigure(0, minsize=50)
# window.columnconfigure([0, 1, 2, 3], minsize=50)
#
# label1 = tk.Label(text="1", bg="black", fg="white")
# label2 = tk.Label(text="2", bg="black", fg="white")
# label3 = tk.Label(text="3", bg="black", fg="white")
# label4 = tk.Label(text="4", bg="black", fg="white")
#
# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1, sticky="ew")
# label3.grid(row=0, column=2, sticky="ns")
# label4.grid(row=0, column=3, sticky="nsew")
#
# window.mainloop()

# --------------------

# # Exercice: B
# # https://realpython.com/python-gui-tkinter/#controlling-layout-with-geometry-managers
# # Below is an image of an address entry form made with Tkinter.
# # An address entry form window built with Tkinter
# #
# # Write a complete script that re-creates the window. You may use any geometry manager you like.
#
# window.geometry("590x240")
# window.title("Address Entry Form")
#
# labels = ["First Name",
#           "Last Name",
#           "Address Line1",
#           "Address Line2",
#           "City",
#           "State/Province",
#           "Postal Code",
#           "Country"]
# initial_frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5, width=590, height=242)
# foot_frame = tk.Frame(master=window, width=560, height=20)
# midle_frame = tk.Frame(master=window, borderwidth=1, width=590, height=280)
#
#
# for i in range(len(labels)):
#
#     frame = tk.Frame(master=midle_frame, borderwidth=1)
#     frame.grid(row=i, sticky="e")
#     label = tk.Label(master=frame, text=labels[i])
#     label.grid(row=i)
#
#     for j in range(1, 2):
#         frame = tk.Frame(master=midle_frame, relief=tk.RAISED, borderwidth=1)
#         frame.grid(row=i, column=j)
#         entry = tk.Entry(master=frame, width=80, bg="white")
#         entry.pack(side=tk.RIGHT)
#
#
# initial_frame.grid(row=1, sticky="n")
# midle_frame.grid(row=1, pady=5, sticky="n")
# foot_frame.grid(row=1, padx=5, sticky="se")
#
# label1 = tk.Label(master=foot_frame, relief=tk.RAISED, borderwidth=2, width=84, height=2)
# button1 = tk.Button(master=foot_frame, text="Submit")
# button2 = tk.Button(master=foot_frame, text="Clear")
#
# label1.grid()
# button1.grid(row=0, sticky="e", padx=10)
# button2.grid(row=0, sticky="e", padx=70)
# window.mainloop()
#
# #####################
# # Solution possible #
# #####################
#
# # Create a new window with the title "Address Entry Form"
# window = tk.Tk()
# window.title("Address Entry Form")
#
# # Create a new frame `frm_form` to contain the Label
# # and Entry widgets for entering address information.
# frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# # Pack the frame into the window
# frm_form.pack()
#
# # List of field labels
# labels = [
#     "First Name:",
#     "Last Name:",
#     "Address Line 1:",
#     "Address Line 2:",
#     "City:",
#     "State/Province:",
#     "Postal Code:",
#     "Country:",
# ]
#
# # Loop over the list of field labels
# for idx, text in enumerate(labels):
#     # Create a Label widget with the text from the labels list
#     label = tk.Label(master=frm_form, text=text)
#     # Create an Entry widget
#     entry = tk.Entry(master=frm_form, width=50)
#     # Use the grid geometry manager to place the Label and
#     # Entry widgets in the row whose index is idx
#     label.grid(row=idx, column=0, sticky="e")
#     entry.grid(row=idx, column=1)
#
# # Create a new frame `frm_buttons` to contain the
# # Submit and Clear buttons. This frame fills the
# # whole window in the horizontal direction and has
# # 5 pixels of horizontal and vertical padding.
# frm_buttons = tk.Frame()
# frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
#
# # Create the "Submit" button and pack it to the
# # right side of `frm_buttons`
# btn_submit = tk.Button(master=frm_buttons, text="Submit")
# btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
#
# # Create the "Clear" button and pack it to the
# # right side of `frm_buttons`
# btn_clear = tk.Button(master=frm_buttons, text="Clear")
# btn_clear.pack(side=tk.RIGHT, ipadx=10)
#
# # Start the application
# window.mainloop()

# --------------------

# # Create an event handler
# def handle_keypress(event):
#     """Print the character associated to the key pressed"""
#     print(event.char)
#
#
# # Bind keypress event to handle_keypress()
# window.bind("<Key>", handle_keypress)

# --------------------

# def handle_click(event):
#     print("The button was clicked!")
#
#
# button = tk.Button(text="Click me!")
#
# button.bind("<Button-1>", handle_click)
#
# button.pack()
#
# # Run the event loop
# window.mainloop()

# --------------------

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()