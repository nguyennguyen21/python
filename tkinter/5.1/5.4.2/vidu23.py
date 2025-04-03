from tkinter import *

window = Tk()
def btn_click():
    lbl.configure(text='button was clicked !!')
window.title("welcome the first app")

window.geometry("350x200")
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
btn = Button(window, text="click me",command= btn_click)
btn.grid(column=1, row = 0)
window.mainloop()