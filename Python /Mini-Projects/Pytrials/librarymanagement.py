class student():
    def __init__(self,name,id):
        self.name=name
        self.id=id
        issued=list()
        issues = 0
class studentSE(student):
    issued = list()
    issues=0
    def __init__(self,name,id):
        super().__init__(self,name,id)
        self.name = name
        self.id = id
        max = 4
        year = 2

class studentTE(student):
    def __init__(self,name,id):
        super(self).__init__(self,name,id)
        max = 6
        year = 3

class book():
    def __init__(self,name,isbn,count):
        self.name=name
        self.isbn=isbn
        self.count=count

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

    def getPosnInList(self,lst,name):
        flag=0
        for k in range(0,len(lst),1):
            if lst[k].name==name:
                flag=1
                break
        if flag==0:
            k=-1
        return k
    def register(self,se,te):
        name = raw_input("Enter the username you wish to enroll with:")
        year=int(raw_input("Which year are you studying in? ie.2nd or 3rd?"))
        if year==2:
            se.append(studentSE(name,i+1))
        elif year==3:
            te.append(studentTE(name,j+1))
    def unregister(self,se,te):
        name = raw_input("Enter the username you wish to unregister:" )
        s=masteraccess.getPosnInList(self,se,name)
        t= masteraccess.getPosnInList(self, te, name)
        if s>=0:
            se.remove(s)
        if t>=0:
            te.remove(t)
    def getStudentDetails(self,se,te):
        try:
            name = raw_input("Enter the name of the student:")
            k=masteraccess.getPosnInList(se,name)
            if k>=0:
                if se(k).name==name:
                    print("Name: " + se(k).name + " Id: " + se(k).id + " No of copies issued:" + se(k).issues,"The books issued are:",se(k).issued)
                    print("The student has currently issued the following books: ",se(k).issued)
            t=masteraccess.getPosnInList(te,name)
            if k>=0:
                if te(t).name==name:
                    print("Name: "+te(t).name+" Id: "+te(t).id+" No of copies issued:"+te(t).issues)
                    print("The student has currently issued the following books: ", te(t).issued)
            if k==-1 and t==-1:
                print("Student doesnt exist in records.....")

        except KeyError:
            print("Error Occured....Username may not exist...")

    def addbook(self,books,b):
        try:
            name = raw_input("Enter the name of the book you wish to add: ")
            no = int(raw_input("How many book to add?"))
            books.append(book(name, b + 1, no))
        except TypeError:
            print("Invalid number by default 1 book added....")
            books.append(book(name, b + 1, 1))

    def removebook(self,books):
        try:
            name = raw_input("Enter the name of the book you wish to delete: ")
            b=masteraccess.getPosnInList(self,books,name)
            if b>=0:
                books.remove(b)
            else:
                print("Invalid book...")
        except KeyError:
            print("Error occured while deleting.....Book may not exist :-(")

    def issuebook(self,books,se,te):
        try:
            name = raw_input("Enter the name of the book you wish to issue: ")
            k=masteraccess.getPosnInList(self,books,name)
            if k>=0:
                na=raw_input("Enter your name: ")
                s=masteraccess.getPosnInList(self,se,na)
                t=masteraccess.getPosnInList(self,te,na)
                if s>=0:
                    se[s].issued.append(books[k].name)
                    se[s].issues=se[s].issues-1
                if t>=0:
                    se(t).issued.append(books[t].name)
                    se(t).issues=se[t].issues-1
                if s==-1 and k==-1:
                    print("Invalid name")
            else:
                print("Book not available in stock.......")

        except KeyError:
            print("An error occured....The book may not exist...")

    def returnbook(self,books,se,te):
        try:
            name = raw_input("Enter the name of the book you wish to return: ")
            k=masteraccess.getPosnInList(books,name)
            if k>=0:
                if books(k).count>= 5:
                    print("Book stock full, Cannot accept more books.....")
                else:
                    uname = raw_input("Enter ur username:")
                    t=masteraccess.getPosnInList(te,uname)
                    s=masteraccess.getPosnInList(se,uname)
                    if t>=0:
                        te(t).issued.remove(uname)
                        te(t).issues=te(t).issues-1
                    elif s>= 0:
                        se(s).issued.remove(uname)
                        se(s).issues = se(s).issues - 1

                    else:
                        print("Username not registered....Register into the library before issuing...")
            else:
                print("Invalid Book")
        except KeyError:
            print("Error occurred.....Book may not exist......")

    def display(self,se,te,books):
        print("The Library has the following books: ")
        for k in range(0,len(books),1):
            print("isbn: ",books[k].isbn," Name: ",books[k].name," Copies: ",books[k].count)
        print("Member details are: ")
        for k in range(0,len(se),1):
            print("Name: "+se[k].name+" Id: "+str(se[k].id)+" No of copies issued:"+str(se[k].issues)+"The books issued are:",se[k].issued)

    def accesslib(self,se,te,books):
        choice = 1
        print(
            "Menu:\n1=Issue \n2=Return \n3=Add new book \n4=Delete a book\n5=Unregister \n6=Register\n7=Get user details")
        while choice >= 1 and choice <= 8:
            try:
                choice = int(raw_input("Enter your choice:"))
            except ValueError:
                print("Error Occurred in choice....")
            if choice == 1:
                masteraccess.issuebook(self,books,se,te)
            elif choice == 2:
                masteraccess.returnbook(self,books,se,te)
            elif choice == 3:
                masteraccess.addbook(self,books,b)
            elif choice == 4:
                masteraccess.removebook(self,books,se,te)
            elif choice == 5:
                masteraccess.unregister(self,se,te)
            elif choice == 6:
                masteraccess.register(self,se,te)
            elif choice == 7:
                masteraccess.getStudentDetails(self,se,te)
            elif choice==8:
                masteraccess.display(self,se,te,books)
            else:
                print("Invalid choice...Exiting program....")
                masteraccess.display(se,te,books)
def main():
    m=masteraccess()
    masteraccess.accesslib(m,[],[],[])

main()