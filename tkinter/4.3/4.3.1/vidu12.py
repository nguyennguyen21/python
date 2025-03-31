
from tkinter import *
window = Tk()

window.title("welcome to First app")
window.geometry('300x140')
name = Label(window,text="User Name").place(x = 50,y=10)
email = Label(window,text="Email").place(x=50,y = 40)


Password = Label(window,text="Password").place(x = 50,y=70)
etn1 = Entry(window).place(x=115,y=10)
etn2 = Entry(window).place(x=115,y=40)
etn3 = Entry(window).place(x=115,y=70)


btn = Button(window,text="Submit").place(x=125,y=100)

window.mainloop()
