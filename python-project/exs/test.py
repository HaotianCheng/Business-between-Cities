
from tkinter import *

master = Tk()

w = Scale(master, from_=0, to=100, length = 100, showvalue = 0)
w.pack()

w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()

mainloop()
