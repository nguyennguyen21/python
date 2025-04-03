from tkinter import *

def draw(canvas,line_distance):
    for i in range(9):
        canvas.create_line(line_distance * i, 0, line_distance * i, line_distance*8)
        canvas.create_line(0, line_distance * i, line_distance*8, line_distance * i)

window = Tk()
l_d = 100
w = Canvas(window,width=410,height=410)
w.pack()
draw(w,l_d)
window.mainloop()