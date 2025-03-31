import tkinter as tk 
mainWindow = tk.Tk()
logo = tk.PhotoImage(file=r"C:/Users/HIU_PM06_25/Downloads/background-4793186_1280.png") 
wLbl1 = tk.Label(mainWindow, image=logo).pack(side="right")
content = "Hiện tại, tkinter chỉ hỗ trợ các định dạng GIF và PPM/PGM."
wLbl2 = tk.Label(mainWindow, justify=tk.LEFT, padx = 10, text=content).pack(side="left")
mainWindow.mainloop()
