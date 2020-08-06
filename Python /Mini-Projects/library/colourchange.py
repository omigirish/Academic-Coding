from tkinter import *
root=Tk()
root.geometry('2000x2000')
root.title('Colours')
def red(self):
    b1["bg"]="Red"

def blue(self):
    b2["bg"]="Blue"

def yellow(self):
    b3["bg"]="Yellow"

def azure(self):
    b4["bg"]="Azure"

def green(self):
    b5["bg"]="Green"

def gold(self):
    b6["bg"]="Gold"

b1=Button(root,text='Red',highlightbackground="red", command=red)
b1.place(x=50,y=100)
b2=Button(root,text='Blue')
b2.place(x=100,y=100)
b3=Button(root,text='Yellow')
b3.place(x=150,y=100)
b4=Button(root,text='Azure')
b4.place(x=50,y=200)
b5=Button(root,text='Green')
b5.place(x=100,y=200)
b6=Button(root,text='Gold')
b6.place(x=150,y=200)


'''b1.bind("<Button-1>",red)
b2.bind("<Button-1>",blue)
b3.bind("<Button-1>",yellow)
b4.bind("<Button-1>",azure)
b5.bind("<Button-1>",green)
b6.bind("<Button-1>",gold)'''


root.mainloop()
