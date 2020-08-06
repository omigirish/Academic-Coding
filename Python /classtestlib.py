class library():
    def __init__(self,lib,reg):
        self.lib=lib
        self.reg=reg
    def addbook(sel,lib):
        try:
            name = input("Enter the name of the book you wish to add: ")
            no = int(input("How many book to add?"))
            lib.update({name: no})
        except TypeError:
            print("Invalid number by default 5 books added....")
            lib.update({name: 5})


    def removebook(self,lib):
        try:
            name = input("Enter the name of the book you wish to delete: ")
            del lib[name]
        except KeyError:
            print("Error occured while deleting.....Book may not exist :-(")


    def issuebook(self,lib,reg):
        try:
            name = input("Enter the name of the book you wish to issue: ")
            if (lib[name] <= 0):
                print("Book not available in stock.......")
            else:
                uname = input("Enter ur username:")
                if uname in reg.keys():
                    lib[name] = lib[name] - 1
                    reg[uname].append(name)
                else:
                    print("Username not registered....Register into the library before issuing...")
        except KeyError:
            print("An error occured....The book may not exist...")


    def returnbook(self,lib,reg):
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


    def register(self,reg):
        name = input("Enter the username you wish to enroll with:")
        reg.update({name: []})


    def findbook(self,lib):
        try:
            name = input("Enter the name of the book you wish to find: ")
            print("No of Copies available of book: ", name, "is=", lib[name])
        except KeyError:
            print("Error Occurred.....Book may not exist....")


    def getdetails(self,reg):
        try:
            name = input("Enter the name of the user whose details are required:")
            print(reg[name])
        except KeyError:
            print("Error Occured....Username may not exist...")
    def accesslib(self,lib,reg):
        choice = 1
        print(
            "Menu:\n1=Issue \n2=Return \n3=Add new book \n4=Delete a book\n5=Get book details\n6=Register\n7=Get user details")
        while choice >= 1 and choice <= 7:
            try:
                choice = int(input("Enter your choice:"))
            except ValueError:
                print("Error Occurred in choice....")
            if choice == 1:
                library.issuebook(self,lib,reg)
            elif choice == 2:
                library.returnbook(self,lib,reg)
            elif choice == 3:
                library.addbook(self,lib)
            elif choice == 4:
                library.removebook(self,lib)
            elif choice == 5:
                library.findbook(self,lib)
            elif choice == 6:
                library.register(self,reg)
            elif choice == 7:
                library.getdetails(self,reg)
            else:
                print("Invalid choice...Exiting program....")
                print("The current status of the Library is:")
                print(lib)

def main():
    lib = {"Python": 4, "Java": 4, "C++": 5}
    reg = {"Girish": ["Python", "Java"], "Sushant": []}
    lib1=library(lib,reg)
    lib1.accesslib(lib1.lib,lib1.reg)
main()
