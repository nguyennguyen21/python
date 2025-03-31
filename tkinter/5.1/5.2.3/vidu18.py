
import tkinter as tk 
mainWindow = tk.Tk()
tk.Label(mainWindow, text="Red Text in Times Font",
fg = "red",
font = "Times").pack() 
tk.Label(mainWindow, 
text="Green Text in Helvetica Font",
fg = "light green", bg = "dark green",
font = "Helvetica 16 bold italic").pack() 
tk.Label(mainWindow, text="Blue Text in Verdana bold",
fg = "blue", 
bg = "yellow",
font = "Verdana 10 bold").pack() 
mainWindow.mainloop()
