from tkinter import *
window=Tk()
window.geometry("500x300")
window.title("Drawing board")
def red():
    c.itemconfigure(x,fill="red")
    c.itemconfigure(y, fill="red")
    c.itemconfigure(z, fill="red")

def green():
    c.itemconfigure(x, fill="green")
    c.itemconfigure(y, fill="green")
    c.itemconfigure(z, fill="green")


def blue():
    c.itemconfigure(x, fill="blue")
    c.itemconfigure(y, fill="blue")
    c.itemconfigure(z, fill="blue")


def drect():
    c.itemconfigure(x, state="normal")
    c.itemconfigure(y, state="hidden")
    c.itemconfigure(z, state="hidden")


def dcirc():
    c.itemconfigure(x, state="hidden")
    c.itemconfigure(y, state="normal")
    c.itemconfigure(z, state="hidden")
def dtri():
    c.itemconfigure(x, state="hidden")
    c.itemconfigure(y, state="hidden")
    c.itemconfigure(z, state="normal")



c=Canvas(window,height=200,width=200)
c.place(x=250,y=50)
b1=Button(window,text="   RED   ",command=red)
b1.place(x=10,y=50)
b2=Button(window,text=" GREEN ",command=green)
b2.place(x=10,y=100)
b3=Button(window,text="  BLUE  ",command=blue)
b3.place(x=10,y=150)


b4=Button(window,text="   CIRCLE   ",command=dcirc)
b4.place(x=100,y=50)
b5=Button(window,text=" TRIANGLE ",command=dtri)
b5.place(x=100,y=100)
b6=Button(window,text="  RECTANGLE  ",command=drect)
b6.place(x=100,y=150)


x=c.create_rectangle(0, 0, 200, 200)
y=c.create_oval(200, 200, 5, 5)
z=c.create_polygon(0, 0, 200, 200, 200, 0)
c.itemconfigure(x, state="hidden")
c.itemconfigure(y, state="hidden")
c.itemconfigure(z, state="hidden")


window.mainloop()