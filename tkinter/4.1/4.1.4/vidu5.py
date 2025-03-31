# sử dụng padding y
import tkinter as tk
window = tk.Tk()

w = tk.Label(window, text="red sun", bg ="red",fg="white" )
w.pack(fill=tk.X,pady=10)
w = tk.Label(window, text="Green Grass", bg ="green",fg="black" )
w.pack(fill=tk.X,pady=20)
w = tk.Label(window, text="Blue Sky", bg ="Blue", fg="white" )
w.pack(fill=tk.X,pady=30)
w.mainloop()