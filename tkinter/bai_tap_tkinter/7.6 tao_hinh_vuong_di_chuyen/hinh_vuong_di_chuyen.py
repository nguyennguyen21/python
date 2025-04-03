import tkinter as tk 
def hinh_vuong_di_chuyen(sukien):
    #ta cần lấy tọa đô
    toa_do_hien_tai = canvas.coords(hinh_vuong)
    x1,y1,x2,y2 = toa_do_hien_tai
    if sukien.keysym == "w":
        canvas.coords(hinh_vuong,x1,y1-10,x2,y2-10)
    if sukien.keysym == "s":
        canvas.coords(hinh_vuong,x1,y1+10,x2,y2+10)
    if sukien.keysym == "a":
        canvas.coords(hinh_vuong,x1-10,y1,x2-10,y2)
    if sukien.keysym == "d":
        canvas.coords(hinh_vuong,x1+10,y1,x2+10,y2)
    
    
    
    
window = tk.Tk()

canvas = tk.Canvas(window,width=500,height=500)
canvas.pack()
hinh_vuong = canvas.create_rectangle(150,150,200,200,fill="black")
window.bind("<Key>", hinh_vuong_di_chuyen)
window.mainloop()
    