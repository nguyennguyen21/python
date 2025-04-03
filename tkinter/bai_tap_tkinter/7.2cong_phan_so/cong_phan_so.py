#Bài 7.2
import random
from tkinter import *
from tkinter import Entry

def cont_click():
    tso1.set(random.randint(1,9))
    tso2.set(random.randint(1,9))
    mso1.set(random.randint(1,9))
    mso2.set(random.randint(1,9))
    ts1.configure(text=tso1.get())
    ts2.configure(text=tso2.get())
    ms1.configure(text=mso1.get())
    ms2.configure(text=mso2.get())

def rutGon(ts,ms):
    for i in range (min(int(ts),int(ms)),0,-1):
        if max(int(ts),int(ms)) % i == 0:
            return int(ts) / i,int(ms)/ i
    return int(ts),int(ms)

def check_click():
    x = ety_tso.get()
    y = ety_mso.get()
    ques_tso = tso1.get()*mso2.get()+tso2.get()*mso1.get()
    ques_mso = mso1.get()*mso2.get()
    ques_tso,ques_mso = rutGon(ques_tso,ques_mso)
    x,y = rutGon(x,y)
    if ques_tso == x and ques_mso == y:
        correct.set(correct.get()+1)
        resT.configure(text=f"Số lần đúng:{correct.get()}")
    else:
        incorrect.set(incorrect.get() + 1)
        resF.configure(text=f"Số lần sai:{incorrect.get()}")
window = Tk()
correct = IntVar()
correct.set(0)
incorrect = IntVar()
incorrect.set(0)
tso1 = IntVar()
tso1.set(0)
tso2 = IntVar()
tso2.set(0)
mso1 = IntVar()
mso1.set(0)
mso2 = IntVar()
mso1.set(0)
ts1 = Label(window,text="")
ts1.grid(row=0,column=0)
ms1 = Label(window,text="")
ms1.grid(row=2,column=0)
al = Label(window,text="+")
al.grid(row=1,column=1)
eq = Label(window,text="=")
eq.grid(row=1,column=3)
ts2 = Label(window,text="")
ts2.grid(row=0,column=2)
ms2 = Label(window,text="")
ms2.grid(row=2,column=2)
ety_tso = Entry(window,width=10)
ety_tso.grid(row=0,column=4)
ety_mso = Entry(window,width=10)
ety_mso.grid(row=2,column=4)
resT = Label(window,text="Số lần đúng:0")
resT.grid(row=3,columnspan=4)
resF = Label(window,text="Số lần sai:0")
resF.grid(row=4,columnspan=4)
checkBtn = Button(window,text="Kiểm tra",command=check_click)
checkBtn.grid(row=5,column=0,columnspan=2)
contBtn = Button(window,text="Tiếp tục",command=cont_click)
contBtn.grid(row=5,column=3,columnspan=2)
window.mainloop()