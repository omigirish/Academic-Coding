""" Make a class student with student name as variable
make a clasas se student and te student
these two classes will inherit the student class both these classes will have a variable called max number of issues
se  can issue 4 books and te can issue 6 books
class master transaction(interactive)
class book will have book name isbn max no of copies available no of copies
"""
class student():
    def __init__(self,name,id):
        self.name=name
        self.id=id
        issued=list()
class studentSE(student):
    max=4
    year=2
    def ___init__(self):
        super()
        issues=0

class studentTE(student):
    max=6
    year=3
    def ___init__(self):
        super()
        issues=0

class book():
    def ___init__(self,bname,isbn,count):
        self.bname=bname
        self.isbn=isbn

class masteraccess():
    global i
    global j
    i=0
    j=0
    global b
    b=0
    se=list()
    te=list()
    books=list()
    list(te)
    def register(self,se,te):
        name = input("Enter the username you wish to enroll with:")
        year=int(input("Which year are you studying in? ie.2nd or 3rd?"))
        if year==2:
            se.append(studentSE(name,i+1))
        elif year==3:
            te.append(studentTE(name,j+1))
    def getdetails(self,se,te):
        f1=0
        f2=0
        try:
            name = input("Enter the name of the user whose details are required:")
            for k in range(0, len(se), 1):
                if se(k).name==name:
                    f1=1
                    print("Name: " + se(k).name + " Id: " + se(k).id + " No of copies issued:" + se(k).issues)
                    break
            for k in range(0,len(te),1):
                if te(k).name==name:
                    f2=1
                    print("Name: "+te(k).name+" Id: "+te(k).id+" No of copies issued:"+te(k).issues)
                    break
            if f1==0 and f2==0:
                print("Student doesnt exist in records.....")
        except KeyError:
            print("Error Occured....Username may not exist...")
    def addbook(self,books,b):
        try:
            name = input("Enter the name of the book you wish to add: ")
            no = int(input("How many book to add?"))

        except TypeError:
            print("Invalid number by default 1 book added....")
            books.append(book(name, b + 1, 1))
    def issuebook(self,books,se,te):
        f1=0
        try:
            name = input("Enter the name of the book you wish to issue: ")
            for k in range(0, len(books), 1):
                if books(k).bname == name:
                    f1 = 1
                    break
            if f1== 0:
                print("Book not available in stock.......")
            else:
                uname = input("Enter ur name:")
                year=int(input("Enter your year:"))
                if year==2:
                    if uname in se.name:
                        books(k).count=books(k).count-1
                else:
                    print("Username not registered....Register into the library before issuing...")
        except KeyError:
            print("An error occured....The book may not exist...")




