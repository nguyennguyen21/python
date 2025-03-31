# sử dụng padx(padding x)
import tkinter as tk
window = tk.Tk()

w = tk.Label(window, text="red sun", bg ="red",fg="white" )
w.pack(fill=tk.X,padx=30)
w = tk.Label(window, text="Green Grass", bg ="green",fg="black" )
w.pack(fill=tk.X,padx=20)
w = tk.Label(window, text="Blue Sky", bg ="Blue", fg="white" )
w.pack(fill=tk.X,padx=10)
w.mainloop()