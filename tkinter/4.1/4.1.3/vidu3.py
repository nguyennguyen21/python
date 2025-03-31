from tkinter import *

window = Tk()

window.title("clock")

window.geometry("200x200")

btn1 = Button(window,text="9",fg="red")
btn1.pack(side=LEFT)
btn2 = Button(window,text="3",fg="black")
btn2.pack(side=RIGHT)
btn3 = Button(window,text="12",fg="black")
btn3.pack(side=TOP)
btn4 = Button(window,text="6",fg="black")
btn4.pack(side=BOTTOM)
window.mainloop()