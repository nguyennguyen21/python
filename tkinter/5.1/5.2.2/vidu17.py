import tkinter as tk 
mainWindow = tk.Tk()
logo = tk.PhotoImage(file="C:/Users/HIU_PM06_25/Downloads/background-4793186_1280.png")
content = "Hiện tại, tkinter chỉ hỗ trợ các định dạng GIF và PPM/PGM."
wLabel3 = tk.Label(mainWindow,compound = tk.CENTER, text= content, image=logo).pack(side="right")
wLbl2 = tk.Label(mainWindow, justify=tk.LEFT, padx = 10, text= content).pack(side="left")
mainWindow.mainloop()

import tkinter as tk 
mainWindow = tk.Tk()
logo = tk.PhotoImage(file="C:/Users/HIU_PM06_25/Downloads/background-4793186_1280.png")
content = "Hiện tại, tkinter chỉ hỗ trợ các định dạng GIF và PPM/PGM."
wLabel3 = tk.Label(mainWindow,compound = tk.CENTER, text= content, image=logo).pack(side="right")
wLbl2 = tk.Label(mainWindow, justify=tk.LEFT, padx = 10, text= content).pack(side="left")
mainWindow.mainloop()

