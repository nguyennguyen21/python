import tkinter as tk

colours =["red","green","orange","white","yellow","blue"]

r = 0
for c in colours:
    tk.Label(text = c,relief=tk.RIDGE,width=15).grid(row=r,column=0)
    tk.Label(bg = c,relief=tk.SUNKEN,width=15).grid(row=r,column=1)
    r +=1
tk.mainloop()