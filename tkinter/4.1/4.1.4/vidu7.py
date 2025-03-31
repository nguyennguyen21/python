# sử dụng ipadding x và ipadding y
import tkinter as tk
window = tk.Tk()

w = tk.Label(window, text="red sun", bg ="red",fg="white" )
w.pack()
w = tk.Label(window, text="Green Grass", bg ="green",fg="black" )
w.pack(ipadx=10)
w = tk.Label(window, text="Blue Sky", bg ="Blue", fg="white" )
w.pack(ipady=20)
w.mainloop()