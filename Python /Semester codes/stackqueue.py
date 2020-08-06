#Q24 Animated stack and queue
#implementation of radio buttons skipped
from tkinter import*
from tkinter import messagebox
slength=0
qlength=0
class node():
    def __init__(self,data=None):
        self.data=data
        self.next=None

class queue():
    def __init__(self):
        self.head=node()
        self.ptr=self.head

    def enqueue(self):     #appends a node to the end of the list
        x=e.get()
        global qlength
        qlength = qlength + 1
        if self.head.data==None:
            self.head.data=x
        else:
            p=node(x)
            self.ptr.next=p
            self.ptr=p

    def dequeue(self):  #removes an element from the beginning of the queue
        if self.head!=None:
            global qlength
            qlength = qlength - 1
            self.head=self.head.next
        else:
            messagebox.showinfo("NOTE!!", "Cannot dequeu....QUEUE IS EMPTY!")

class stack():
    def __init__(self):
        self.head=node()
        self.ptr=self.head

    def push(self):     #appends a node to the end of the list
        global slength
        slength=slength+1
        x=e.get()
        if self.head.data==None:
            self.head.data=x
        else:
            p=node(x)
            p.next=self.ptr
            self.ptr=p
            self.head=p

    def pop(self):  #removes an element from the beginning of the queue
        global slength
        if self.head!=None:
            self.head=self.head.next
            slength=slength-1
        else:
            messagebox.showinfo("NOTE!!", "Cannot POP...STACK IS EMPTY!")
def getslength():
    global slength
    messagebox.showinfo("Information","Length of stack is: "+str(slength))
def getqlength():
    global qlength
    messagebox.showinfo("Information","Length of Queue is: "+str(qlength))

s=stack()
q=queue()



window=Tk()
window.title("Data Structures")
l1=Label(window,text="-")
l1.grid(row=2,column=4)
l2=Label(window,text="-")
l2.grid(row=3,column=4)
l3=Label(window,text="-")
l3.grid(row=4,column=4)
l4=Label(window,text="-")
l4.grid(row=5,column=4)
l5=Label(window,text="-")
l5.grid(row=6,column=4)
l6=Label(window,text="-")
l6.grid(row=7,column=4)
l7=Label(window,text="PUSH/POP VALUE:")
l7.grid(row=1,column=5)
e=Entry(window)
e.grid(row=2,column=5)

label_lst=[l6,l5,l4,l3,l2,l1]
def disps():
    for label in label_lst:
        label.configure(text="-")
    t = s.head
    x=0
    if t == None:
        messagebox.showinfo("NOTE!!","STACK IS EMPTY!")
    while t != None:
        label_lst[x].configure(text=t.data)
        t = t.next
        x=x+1
        print(j.get())

def dispq():
    for label in label_lst:
        label.configure(text="-")
    t = q.head
    x=0
    if t == None:
        messagebox.showinfo("NOTE!","QUEUE IS EMPTY!")
    while t != None:
        label_lst[x].configure(text=t.data)
        t = t.next
        x=x+1
    print()
j=IntVar()
r1=Radiobutton(window,text="STACK",value=1,variable=j)
r1.grid(row=1,column=1)
r2=Radiobutton(window,text="QUEUE",value=2,variable=j)
r2.grid(row=1,column=2)
l1=Label(window,text="ELEMENTS")
l1.grid(row=1,column=3)
b1=Button(window,text="PUSH",command=s.push)
b1.grid(row=2,column=1)
b2=Button(window,text="POP",command=s.pop)
b2.grid(row=3,column=1)
b3=Button(window,text="DISPLAY",command=disps)
b3.grid(row=4,column=1)
b4=Button(window,text="LENGTH",command=getslength)
b4.grid(row=5,column=1)
b5=Button(window,text="ENQUEUE",command=q.enqueue)
b5.grid(row=2,column=2)
b1=Button(window,text="DEQUEUE",command=q.dequeue)
b1.grid(row=3,column=2)
b1=Button(window,text="DISPLAY",command=dispq)
b1.grid(row=4,column=2)
b1=Button(window,text="LENGTH",command=getqlength)
b1.grid(row=5,column=2)


window.mainloop()
