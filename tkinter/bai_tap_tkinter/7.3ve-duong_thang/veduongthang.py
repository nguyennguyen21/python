import tkinter as tk
window = tk.Tk()
def ve_hinh():

       
        x_start = int(e1.get())
        y_start = int(e2.get())
        x_end = int(e3.get())
        y_end = int(e4.get())
        
        
        canvas.delete("all")
        
        
        canvas.create_line(x_start, y_start, x_end, y_end, fill="red", width=2)
Lb1 = tk.Label(window,text="XStart")
Lb1.grid(row=1 , column=0)
e1 = tk.Entry(width=5)
e1.grid(row=1,column=1)

Lb2 = tk.Label(window,text="YStart")
Lb2.grid(row=1 , column=2)
e2 = tk.Entry(width=5)
e2.grid(row=1,column=3)

Lb3 = tk.Label(window,text="XEnd")
Lb3.grid(row=2 , column=0)
e3 = tk.Entry(width=5)
e3.grid(row=2,column=1)

Lb4 = tk.Label(window,text="YEnd")
Lb4.grid(row=2 , column=2)
e4 = tk.Entry(width=5)
e4.grid(row=2,column=3)

btn = tk.Button(window,text="vẽ hình",justify="center",command=ve_hinh)
btn.grid(row=3,column=1)
canvas = tk.Canvas(window, width=300, height=300)
canvas.grid(row=4, column=0, columnspan=4)
window.mainloop()
