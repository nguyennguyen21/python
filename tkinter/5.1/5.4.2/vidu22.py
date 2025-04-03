from tkinter import *

window = Tk()

window.title("welcome the first app")

window.geometry("350x200")
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
btn = Button(window, text="click me",bg="orange",fg="red")
btn.grid(column=1, row = 0)
window.mainloop()