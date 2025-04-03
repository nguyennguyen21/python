import tkinter as tk
from tkinter import *
from tkinter.ttk import *
window = tk.Tk()
def chuyen_doi_cac_he():
    so_thap_phan = e1.get()
    try:
        decimal_number = int(so_thap_phan)  
        if var.get() == 1:  
            result = bin(decimal_number)[2:] 
            res.config(text="Kết quả (Nhị phân): " + result)
        elif var.get() == 2: 
            result = oct(decimal_number)[2:]  
            res.config(text="Kết quả (Bát phân): " + result)
        elif var.get() == 3:  
            result = hex(decimal_number)[2:] 
            res.config(text="Kết quả (Thập lục phân): " + result)
        else:
           res.config(text="Vui lòng chọn hệ số!")
    except ValueError:
        res.config(text="Vui lòng nhập một số hợp lệ!")
        
window.title("chuyển đổi hệ số")
tk.Label(window,text="nhập số thập phân :").grid(row=0)

var = IntVar()
rad1 = Radiobutton(window, text="Nhị phân", variable=var, value=1)
rad1.grid(row=0, column=2)

rad2 = Radiobutton(window, text="Bát phân", variable=var, value=2)
rad2.grid(row=1, column=2)

rad3 = Radiobutton(window, text="Thập lục phân", variable=var, value=3)
rad3.grid(row=2, column=2)
e1 = tk.Entry(window)
e1.grid(row=1, column= 0)

result_label =tk.Label(window,text="kết quả")
result_label.grid(row=2,column=0)
res = tk.Label(window,text="")
res.grid(row=3,column=0)


btn = tk.Button(window, text ="chuyển đổi",width=15,command=chuyen_doi_cac_he).grid(row=4, column=2)
window.mainloop()
