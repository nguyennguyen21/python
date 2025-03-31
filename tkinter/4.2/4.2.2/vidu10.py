
from tkinter import *
window = Tk()

window.title("welcome to First app")
window.geometry('300x80')
name = Label(window,text="User Name").grid(row = 0,column=0)
etn1 = Entry(window).grid(row=0,column=1)

Password = Label(window,text="Password").grid(row = 1,column=0)
etn2 = Entry(window).grid(row=1,column=1)

btn = Button(window,text="Submit").grid(row=4,column=1)

window.mainloop()
