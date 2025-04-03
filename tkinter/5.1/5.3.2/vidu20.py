import tkinter as tk
master = tk.Tk()
 
S ="Whatever you do will be insignificant, but it is very important that you do it. \n(Mahatma Dandhi)"

msg = tk.Message(master, text = S)
msg.config(bg='lightgreen',font=('times',24,'italic'))
msg.pack()
tk.mainloop()