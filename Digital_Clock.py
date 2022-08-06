from tkinter import *
from tkinter.ttk import *

from time import strftime

window = Tk()
window.title('Digitial Python Clock')

clock_label = Label(window, font=('sans',80),background='black',foreground='chartreuse1')
clock_label.pack(anchor='center')

def clock():
    tick = strftime('%H:%M:%S %p')
    clock_label.config(text = tick)
    clock_label.after(1000,clock)

clock()

window.mainloop()