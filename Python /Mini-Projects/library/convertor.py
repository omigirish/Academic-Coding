from tkinter import *
from tkinter import messagebox
def convert():
    x=checked.get()
    qty1=t1.get()
    qty2=t2.get()
    if qty1=="" or qty2=="":
        messagebox.showinfo("Information", "Entries cannot be blank!")
    else:
        if x==1:
            l1['text']="Celsius:"
            l2['text']="Fahrenheit:"
            c1=float(qty1)
            f2=float(qty2)
            f1=float((c1*9/5) + 32)
            c2=float((f2-32)*5/9)
            o1['text']="Fahrenheit= " + str(f1)
            o2['text']="Celsius= " + str(c2)
        elif x==2:
            l1['text']="Rupees:"
            l2['text']="Dollars:"
            r1=float(qty1)
            d2=float(qty2)
            d1=float(0.014*r1)
            r2=float(69.51*d2)
            o1['text']="Dollars= " + str(d1)
            o2['text']="Rupees= " + str(r2)

        elif x==3:
            l1['text']="Kilometers:"
            l2['text']="Miles:"
            k1=float(qty1)
            m2=float(qty2)
            m1=float(0.621*k1)
            k2=float(1.609*m2)
            o1['text']="Miles= " + str(m1)
            o2['text']="Kilometers= " + str(k2)

        else:
            messagebox.showinfo("Information", "Please select a conversion mode!")

def clear():
    l1['text']="Unit1"
    l2['text']="Unit2"
    o1['text'] = "Unit2"
    o2['text'] = "Unit1"
    x.set("0.0")
    y.set("0.0")
    tempc.deselect()
    currc.deselect()
    distc.deselect()

window=Tk("")
window.geometry("600x300+350+80")
window.title("Convertor")
title=Label(window,text="Conversion calculator")
title.place(x=230,y=10)
checked=IntVar()
x=StringVar()
x.set("0.0")
y=StringVar()
y.set("0.0")

tempc=Radiobutton(window,text="Temperature Conversion",value=1,variable=checked,command=convert)
tempc.place(x=50,y=50)
currc=Radiobutton(window,text="Currency Conversion",value=2,variable=checked,command=convert)
currc.place(x=50,y=80)
distc=Radiobutton(window,text="Distance Conversion",value=3,variable=checked,command=convert)
distc.place(x=50,y=110)

l1=Label(window,text="Unit1  :")
l1.place(x=30,y=150)
l2=Label(window,text="Unit2  :")
l2.place(x=30,y=200)
t1=Entry(window,text=x)
t1.place(x=110,y=145)
t2=Entry(window,text=y)
t2.place(x=110,y=195)

o1=Label(window,text="Unit2")
o1.place(x=310,y=150)
o2=Label(window,text="Unit1")
o2.place(x=310,y=200)

b1=Button(window,text=" Convert ",command=convert)
b1.place(x=100,y=250)

b2=Button(window,text="   Clear   ",command=clear)
b2.place(x=200,y=250)

window.mainloop()