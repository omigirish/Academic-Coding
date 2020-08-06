books=[] #CREATING EMPTY LIST
c=0
while(c==0):
    print("1 for adding  new book\n2 for deleting a book\n3 for dislaying total no of books\n4 for dislaying name of books in descending order")
    n=int(input("Enter value:"))
    if(n==1):
        a=input("Enter a book:")
        books.append(a) #APPENDING A NEW VALUE IN THE LIST
    elif(n==2):
        a=input("Enter the book to be deleted:")
        if a in books:
            books.remove(a)#REMOVING A VALUE FROM THE LIST
            print("Book is deleted")
    elif(n==3):
        print("No of books in the list are",len(books)) #PRINTING THE LENGTH OF THE LIST
    elif(n==4):
        books.sort() #SORTING THE LIST
        books.reverse()#REVERSING THE SORTED LIST TO PRINT IN DESCENDING ORDER
        print(books)
    else:
        print("Invalid input")