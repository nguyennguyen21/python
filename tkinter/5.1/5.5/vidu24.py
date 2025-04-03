from tkinter import *
window = Tk()
frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window).pack()
redButton = Button(frame1, text="red",fg="red")
redButton.pack(side=LEFT)
greenButton = Button(frame1,text ="brown",fg="brown")
greenButton.pack(side=LEFT)
blueButton = Button(frame1,text ="blue",fg="blue")
blueButton.pack(side=LEFT)
blueButton = Button(frame2,text ="black",fg="black")
blueButton.pack(side=BOTTOM)
window.mainloop()



