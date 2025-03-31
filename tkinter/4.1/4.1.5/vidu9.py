
import tkinter as tk
window = tk.Tk()

w = tk.Label(window, text="red sun", bg ="red",fg="white" )
w.pack(padx = 5 , side=tk.RIGHT)
w = tk.Label(window, text="Green Grass", bg ="green",fg="black" )
w.pack(padx = 5, pady = 10 , side=tk.RIGHT)
w = tk.Label(window, text="Blue Sky", bg ="Blue", fg="white" )
w.pack(padx = 5, pady = 20 , side=tk.RIGHT)
w.mainloop()