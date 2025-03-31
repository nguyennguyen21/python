
import tkinter as tk 
counter = 0
def counter_label(label): 
def count():
global counter counter += 1
label.config(text=str(counter)) label.after(1000, count)
count()
window = tk.Tk() window.title(“Counting Seconds”) label = tk.Label(window, fg=”green”) label.pack()
counter_label(label)
button = tk.Button(window, text=’Stop’, width=25, command=window.destroy)
button.pack() window.mainloop()
