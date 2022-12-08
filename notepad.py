from tkinter.filedialog import *
from tkinter import *
import tkinter as tk

#UI
canvas = tk.Tk()
canvas.geometry("600x800")
canvas.title("Notepad")
canvas.config(bg='White')
top = Frame(canvas)
top.pack(padx=10, pady=10, anchor='nw')

def saveFile():
    new_file = asksaveasfile(mode='w', filetype=[('text files', '.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()
    
def openFile():
    file = askopenfile(mode='r', filetype=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)
    
def clearFile():
    entry.delete(1.0, END)

#Buttons for Open, Save, Exit and Clear
b1 = Button(canvas, text="Open", bg='White', command=openFile)
b1.pack(in_=top, side=LEFT)

b2 = Button(canvas, text="Save", bg='White', command=saveFile)
b2.pack(in_=top, side=LEFT)

b3 = Button(canvas, text="Clear", bg='White', command=clearFile)
b3.pack(in_=top, side=LEFT)

b4 = Button(canvas, text="Exit", bg='White', command=exit)
b4.pack(in_=top, side=RIGHT)

"""
    wrap automates words at the end of the line
    expand and fill makes sure the entry area covers both screen when expanded
"""
entry = Text(canvas, wrap=WORD, bg='#F9DDA4', font=("poppins", 15))
entry.pack(padx=10, pady=5, expand=TRUE, fill=BOTH)

canvas.mainloop()