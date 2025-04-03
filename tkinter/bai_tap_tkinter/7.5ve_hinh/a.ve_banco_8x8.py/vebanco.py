import tkinter as tk
def vebanco8x8():
   size = 50
   for row in range(8): 
     for col in range(8):
        x1 = col * size
        y1 = row * size
        x2 = x1 + size
        y2 = y1 + size
        if (col + row) % 2 == 0 :
            canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline="black")
        else:
            canvas.create_rectangle(x1,y1,x2,y2,fill="white",outline="black")
window = tk.Tk()

canvas = tk.Canvas(width=400,height=400)
canvas.pack()

vebanco8x8()

window.mainloop()
