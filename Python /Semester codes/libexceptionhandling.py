lib={"Python":4,"Java":4,"C++":5}
reg={"Girish":["Python","Java"],"Sushant":[]}
def addbook(lib):
    try:
        name = input("Enter the name of the book you wish to add: ")
        no=int(input("How many book to add?"))
    except TypeError:
        print("Invalid number by default 5 books added....")
        no=5
        lib.update({name:no})

def removebook(lib):
    try:
        name=input("Enter the name of the book you wish to delete: ")
        del lib[name]
    except KeyError:
        print("Error occured while deleting.....Book may not exist :-(")

def issuebook(lib):
    try:
        name = input("Enter the name of the book you wish to issue: ")
        if(lib[name]<=0):
            print("Book not available in stock.......")
        else:
            uname=input("Enter ur username:")
            if uname in reg.keys():
                lib[name]=lib[name]-1
                reg[uname].append(name)
            else:
                print("Username not registered....Register into the library before issuing...")
    except KeyError:
        print("An error occured....The book may not exist...")
def returnbook(lib):
    try:
        name = input("Enter the name of the book you wish to return: ")
        if (lib[name] >= 5):
            print("Book stock full, Cannot accept more books.....")
        else:
            uname = input("Enter ur username:")

            if uname in reg.keys():
                lib[name] = lib[name] + 1
                reg[uname].remove(name)
            else:
                print("Username not registered....Register into the library before issuing...")
    except KeyError:
        print("Error occurred.....Book may not exist......")

def register():
    name=input("Enter the username you wish to enroll with:")
    reg.update({name:[]})

def findbook(lib):
    try:
        name = input("Enter the name of the book you wish to find: ")
        print("No of Copies available of book: ",name,"is=",lib[name])
    except KeyError:
        print("Error Occurred.....Book may not exist....")

def getdetails():
    try:
        name=input("Enter the name of the user whose details are required:")
        print(reg[name])
    except KeyError:
        print("Error Occured....Username may not exist...")
choice=1
print("Menu:\n1=Issue \n2=Return \n3=Add new book \n4=Delete a book\n5=Get book details\n6=Register\n7=Get user details")
while choice>=1 and choice<=7:
    try:
        choice=int(input("Enter your choice:"))
    except TypeError:
        print("Error Occurred in choice....")
        if choice==1:
            issuebook(lib)
        elif choice==2:
            returnbook(lib)
        elif choice==3:
            addbook(lib)
        elif choice==4:
            removebook(lib)
        elif choice==5:
            findbook(lib)
        elif choice==6:
            register()
        elif choice==7:
            getdetails()
        else:
            print("Invalid choice...Exiting program....")
            print("The current status of the Library is:")
            print(lib)
