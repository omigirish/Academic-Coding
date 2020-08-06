import pymysql as pq
from tkinter import *
from tkinter import messagebox

def add():
    name=e1.get()
    id=e2.get()
    ava=e3.get()
    try:
        db = pq.connect('localhost', 'root', 'Sushant@1234', 'sushant')
        cur =db.cursor()
        query="""insert into python_gui(name,id,ava) values(%s,%s,%s)"""
        values=(name,id,ava)
        cur.execute(query,values)
        db.commit()
        messagebox.showinfo("Information", "book added successfully")
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()
def disp():
    try:
        db = pq.connect('localhost', 'root', 'Sushant@1234', 'sushant')
        cur = db.cursor()
        window.withdraw()
        root = Tk()
        root.geometry('600x600+0+50')

        def get():
            name=u.get()
            que="""select * from python_gui where name='%s'"""%(name)
            cur.execute(que)
            stu=cur.fetchall()
            print("before updating the values are \nNAME={0},BOOK ID={1},AVAILABLE COPIES={2}".format(stu[0][0],stu[0][1],stu[0][2]))
            idddd=stu[0][1]
            idd=stu[0][2]
            u2 = Label(root, text="OLD BOOK ID IS->")
            u2.place(x=50, y=125)

            u3 = Label(root, text="OLD NO OF COPIES ARE->")
            u3.place(x=50, y=210)

            l1 = Label(root, text=idd)
            l1.place(x=250, y=210)

            l0 = Label(root, text=idddd)
            l0.place(x=250, y=125)

            l11 = Label(root, text="ENTER THE NEW BOOK ID->")
            l11.place(x=50, y=300)

            ull = Entry(root)
            ull.place(x=250, y=300)

            l22 = Label(root, text="ENTER THE NEW COPIES OF BOOK->")
            l22.place(x=50, y=370)

            ul2 = Entry(root)
            ul2.place(x=250, y=370)
            def updatee():
                x=ull.get()
                y=ul2.get()
                quee="""update python_gui set id='%s',ava='%s' where name='%s'"""%(x,y,name)
                cur.execute(quee)
                db.commit()
                print("after updating the values=\n NAME={0},BOOK ID={1},AVAILABLE COPIES={2}".format(name,x,y))
                messagebox.showinfo("Information", "BOOK UPDATED successfully")

            b22 = Button(root, text="UPDATE VALUE", bg="red", fg="white", command=updatee)
            b22.place(x=150, y=450)
        u1 = Label(root, text="ENTER THE NAME OF THE BOOK->")
        u1.place(x=50, y=50)
        u = Entry(root)
        u.place(x=250, y=50)
        b11 = Button(root, text="GET DETAILS", fg="white", bg="blue",command=get)
        b11.place(x=50, y=450)
        root.mainloop()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()
def clearScreen():
    x.set("")
    y.set("")
    z.set("")


window=Tk()
window.geometry('600x600+0+50')

x=StringVar()
y=StringVar()
z=StringVar()
l1=Label(window,text="ENTER BOOKS NAME ->")
l1.place(x=100,y=50)

e1=Entry(window,text=x)
e1.place(x=250,y=50)

l2=Label(window,text="BOOK ID->")
l2.place(x=100,y=100)

e2=Entry(window,text=y)
e2.place(x=250,y=100)

l3=Label(window,text="NUMBER OF BOOKS->")
l3.place(x=100,y=150)

e3=Entry(window,text=z)
e3.place(x=250,y=150)

b2=Button(window,text="UPDATE BOOK",bg="red",fg="white",command=disp)
b2.place(x=200,y=400)

b3=Button(window,text="CLEAR",bg="yellow",fg="red",command=clearScreen)
b3.place(x=350,y=400)

b1=Button(window,text="ADD BOOK",fg="white",bg="blue",command=add)
b1.place(x=100,y=400)

window.mainloop()
