import tkinter as tk
window = tk.Tk()

w = tk.Label(window, text="red sun", bg ="red",fg="white" )
w.pack(fill = tk.X)
w = tk.Label(window, text="Green Grass", bg ="green",fg="black" )
w.pack(fill = tk.X)
w = tk.Label(window, text="Blue Sky", bg ="Blue", fg="white" )
w.pack(fill = tk.X)
w.mainloop()