import tkinter

t = ()
list = [('R1', 'Anuj', 'Nov', 450, 'Res'), ('R1', 'Anuj', 'June', 80, 'Res'), ('R1', 'Anuj', 'May', 150, 'Res'),
        ('C1', 'Pranav', 'Jan', 250, 'Com'), ('R2', 'Pranav', 'Jan', 400, 'Res'), ('R2', 'Pranav', 'Sept', 500, 'Res'),
        ('C1', 'Janhavi', 'July', 300, 'Com'), ('C2', 'Janhavi', 'Jan', 120, 'Com'), ('C2', 'Janhavi', 'Feb', 250, 'Com')]

root = tkinter.Tk()
root.geometry("600x400")
root.title("Electricity Consumption")


def add():
    w1 = tkinter.Toplevel()
    w1.geometry("600x400")
    w1.title("ADD USER")
    l1 = tkinter.Label(w1, text="Enter ID")
    l1.place(anchor=tkinter.CENTER, relx=0.28, rely=0.2)
    l2 = tkinter.Label(w1, text="Enter Name")
    l2.place(anchor=tkinter.CENTER, relx=0.3, rely=0.3)
    l3 = tkinter.Label(w1, text="Enter Month")
    l3.place(anchor=tkinter.CENTER, relx=0.3, rely=0.4)
    l4 = tkinter.Label(w1, text="Enter Units")
    l4.place(anchor=tkinter.CENTER, relx=0.3, rely=0.5)
    v1 = tkinter.StringVar()
    v2 = tkinter.StringVar()
    v3 = tkinter.StringVar()
    v4 = tkinter.StringVar()
    v5 = tkinter.StringVar()

    e1 = tkinter.Entry(w1, textvariable=v1)
    e1.place(anchor=tkinter.CENTER, relx=0.5, rely=0.2)
    e2 = tkinter.Entry(w1, textvariable=v2)
    e2.place(anchor=tkinter.CENTER, relx=0.5, rely=0.3)
    e3 = tkinter.Entry(w1, textvariable=v3)
    e3.place(anchor=tkinter.CENTER, relx=0.5, rely=0.4)
    e4 = tkinter.Entry(w1, textvariable=v4)
    e4.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)

    def addcus():
        id = v1.get()
        name = v2.get()
        month = v3.get()
        units = int(v4.get())
        type = v5.get()
        if (type == 'Residential'):
            type = 'Res'
        elif (type == 'Commercial'):
            type = 'Com'
        t = (id, name, month, units, type)
        list.append(t)
        print(list)

    b5 = tkinter.Button(w1, text="Enter", command=addcus)
    b5.place(anchor=tkinter.CENTER, relx=0.6, rely=0.8)
    v5.set("Select Type")

    def clear():
        v1.set("")
        v2.set("")
        v3.set("")
        v4.set("")
        v5.set("Select Type")

    b6 = tkinter.Button(w1, text="Clear", command=clear)
    b6.place(anchor=tkinter.CENTER, relx=0.5, rely=0.8)
    dm1 = tkinter.OptionMenu(w1, v5, "Residential", "Commercial")
    dm1.place(anchor=tkinter.CENTER, relx=0.4, rely=0.6)

    b7 = tkinter.Button(w1, text="Back", command=w1.withdraw)
    b7.place(anchor=tkinter.CENTER, relx=0.4, rely=0.8)


def delete():
    w3 = tkinter.Toplevel()
    w3.geometry("600x400")
    w3.title("Delete Entry")
    l6 = tkinter.Label(w3, text="Enter Id")
    l6.place(anchor=tkinter.CENTER, relx=0.275, rely=0.3)
    l7 = tkinter.Label(w3, text="Enter Month")
    l7.place(anchor=tkinter.CENTER, relx=0.3, rely=0.4)
    v6 = tkinter.StringVar()
    v7 = tkinter.StringVar()
    e6 = tkinter.Entry(w3, textvariable=v6)
    e6.place(anchor=tkinter.CENTER, relx=0.5, rely=0.3)
    e7 = tkinter.Entry(w3, textvariable=v7)
    e7.place(anchor=tkinter.CENTER, relx=0.5, rely=0.4)

    def delcus():
        id = v6.get()
        month = v7.get()
        for i in list:
            if id in i:
                if month in i:
                    list.remove(i)
        print(list)

    b8 = tkinter.Button(w3, text="Delete", command=delcus)
    b8.place(anchor=tkinter.CENTER, relx=0.6, rely=0.5)

    def clear():
        v6.set("")
        v7.set("")

    b9 = tkinter.Button(w3, text="Clear", command=clear)
    b9.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)

    b10 = tkinter.Button(w3, text="Back", command=w3.withdraw)
    b10.place(anchor=tkinter.CENTER, relx=0.4, rely=0.5)


def calculate(x):
    a = 0
    if x > 200:
        a = x - 200
        a = a * 15 + 100 * 12 + 100 * 10
    elif x > 100:
        a = x - 100
        a = a * 12 + 100 * 10
    else:
        a = x * 10
    return a


def bill():
    w2 = tkinter.Toplevel()
    w2.geometry("600x400")
    w2.title("Monthly Bill")
    txt = tkinter.Text(w2, height=15, width=60)
    txt.place(anchor=tkinter.CENTER, relx=0.5, rely=0.55)
    l8 = tkinter.Label(w2, text="Enter Name")
    l8.place(anchor=tkinter.CENTER, relx=0.3, rely=0.1)

    v8 = tkinter.StringVar()
    v9 = tkinter.StringVar()
    e8 = tkinter.Entry(w2, textvariable=v8)
    e8.place(anchor=tkinter.CENTER, relx=0.5, rely=0.1)
    v9.set("Select Type")
    dm1 = tkinter.OptionMenu(w2, v9, "Residential", "Commercial")
    dm1.place(anchor=tkinter.CENTER, relx=0.7, rely=0.1)

    def billcus():
        name = v8.get()
        type = v9.get()
        if (type == 'Residential'):
            type = 'Res'
        elif (type == 'Commercial'):
            type = 'Com'
        for i in list:
            if name in i:
                if i[4] == type:
                    x = i[3]
                    a = calculate(x)
                y = "the bill of " + i[2] + " is " + str(a)
                txt.insert(tkinter.INSERT, y + "\n")

    b11 = tkinter.Button(w2, text="Enter", command=billcus)
    b11.place(anchor=tkinter.CENTER, relx=0.6, rely=0.95)
    b12 = tkinter.Button(w2, text="Back", command=w2.withdraw)
    b12.place(anchor=tkinter.CENTER, relx=0.5, rely=0.95)

    def clear():
        v8.set("")
        v9.set("Select Type")
        txt.delete('1.0', tkinter.END)

    b13 = tkinter.Button(w2, text="Clear", command=clear)
    b13.place(anchor=tkinter.CENTER, relx=0.4, rely=0.95)


def tbill():
    w4 = tkinter.Toplevel()
    w4.geometry("600x400")
    w4.title("Total Bill")
    v11 = tkinter.StringVar()
    txt = tkinter.Text(w4, height=15, width=60)
    txt.place(anchor=tkinter.CENTER, relx=0.5, rely=0.55)
    v10 = tkinter.StringVar()
    v10.set("Select Type")
    dm3 = tkinter.OptionMenu(w4, v10, "Residential", "Commercial")
    dm3.place(anchor=tkinter.CENTER, relx=0.4, rely=0.06)

    def tbillcus():
        type = v10.get()
        if (type == 'Residential'):
            type = 'Res'
        elif (type == 'Commercial'):
            type = 'Com'
        s1 = set()
        sum = 0
        a = 0
        for i in list:
            if i[4] == type:
                s1.add(i[1])
        for j in s1:
            for k in list:
                if j in k:
                    if k[4] == type:
                        x = k[3]

                        a = calculate(x)
                        sum = sum + a
            y = "The total of " + j + " is " + str(sum)
            txt.insert(tkinter.INSERT, y + "\n")

    b14 = tkinter.Button(w4, text="Enter", command=tbillcus)
    b14.place(anchor=tkinter.CENTER, relx=0.6, rely=0.95)
    b15 = tkinter.Button(w4, text="Back", command=w4.withdraw)
    b15.place(anchor=tkinter.CENTER, relx=0.5, rely=0.95)

    def clear():
        v10.set("Select Type")
        txt.delete('1.0', tkinter.END)

    b15 = tkinter.Button(w4, text="Clear", command=clear)
    b15.place(anchor=tkinter.CENTER, relx=0.4, rely=0.95)


b1 = tkinter.Button(root, text="Add Entry", command=add)
b1.place(anchor=tkinter.CENTER, relx=0.3, rely=0.2)
b2 = tkinter.Button(root, text="Delete Entry", command=delete)
b2.place(anchor=tkinter.CENTER, relx=0.31, rely=0.3)
b3 = tkinter.Button(root, text="Show Montly usage of customer", command=bill)
b3.place(anchor=tkinter.CENTER, relx=0.4, rely=0.4)
b4 = tkinter.Button(root, text="Show total bill of all cusomers", command=tbill)
b4.place(anchor=tkinter.CENTER, relx=0.39, rely=0.5)

root.mainloop()