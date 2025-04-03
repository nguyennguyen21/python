import tkinter as tk
window = tk.Tk()
tk.Label(window,text="First Name").grid(row=0)
tk.Label(window,text="Last Name").grid(row=1)
e1 = tk.Entry(window)
e2 = tk .Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
window.mainloop()