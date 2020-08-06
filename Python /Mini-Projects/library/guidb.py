import pymysql as pq
from tkinter import *
from tkinter import messagebox

def add():
    name=e1.get()
    id=e2.get()
    qty=e3.get()
    try:
        db = pq.connect('localhost', 'root', 'Girish1234', 'library')
        cur =db.cursor()
        query="""insert into books(name,id,qty) values(%s,%s,%s)"""
        values=(name,id,qty)
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
        db = pq.connect('localhost', 'root', 'Girish1234', 'library')
        cur = db.cursor()
        window.withdraw()
        root = Tk()
        root.title("Update Book")
        root.geometry('520x340+400+150')

        def get():
            name=u.get()
            que="""select * from books where name='%s'"""%(name)
            cur.execute(que)
            stu=cur.fetchall()
            print("before updating the values are \nNAME={0},BOOK ID={1},AVAILABLE COPIES={2}".format(stu[0][0],stu[0][1],stu[0][2]))
            idddd=stu[0][1]
            idd=stu[0][2]
            u2 = Label(root, text="OLD BOOK_ID:")
            u2.place(x=50, y=100)

            u3 = Label(root, text="NO. OF COPIES:")
            u3.place(x=50, y=150)

            l1 = Label(root, text=idd)
            l1.place(x=160, y=150)

            l0 = Label(root, text=idddd)
            l0.place(x=160, y=100)

            l11 = Label(root, text="NEW BOOK ID:")
            l11.place(x=50, y=200)

            ull = Entry(root)
            ull.place(x=160, y=200)

            l22 = Label(root, text="No of Copies:")
            l22.place(x=50, y=250)

            ul2 = Entry(root)
            ul2.place(x=160, y=250)
            def updatee():
                x=ull.get()
                y=ul2.get()
                quee="""update books set id='%s',qty='%s' where name='%s'"""%(x,y,name)
                cur.execute(quee)
                db.commit()
                print("after updating the values=\n NAME={0},BOOK ID={1},AVAILABLE COPIES={2}".format(name,x,y))
                messagebox.showinfo("Information", "BOOK UPDATED successfully")

            b22 = Button(root, text="UPDATE VALUE",command=updatee)
            b22.place(x=365, y=225)
        u1 = Label(root, text="Book Name:")
        u1.place(x=50, y=50)
        u=Entry(root)
        u.place(x=160, y=50)
        b11 = Button(root, text="GET DETAILS",command=get)
        b11.place(x=365, y=55)
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


window=Tk("")
window.geometry('400x300+480+220')
window.title("ADD BOOK")
x=StringVar()
y=StringVar()
z=StringVar()
l1=Label(window,text="Book Name:")
l1.place(x=50,y=50)

e1=Entry(window,text=x)
e1.place(x=150,y=50)

l2=Label(window,text="BOOK ID:")
l2.place(x=50,y=100)

e2=Entry(window,text=y)
e2.place(x=150,y=100)

l3=Label(window,text="No. Of Books:")
l3.place(x=50,y=150)

e3=Entry(window,text=z)
e3.place(x=150,y=150)

b2=Button(window,text="UPDATE BOOK",fg='black',command=disp)
b2.place(x=160,y=210)

b3=Button(window,text="CLEAR",command=clearScreen,fg='red')
b3.place(x=290,y=210)

b1=Button(window,text="ADD BOOK",command=add)
b1.place(x=50,y=210)

window.mainloop()
