l1=['Vinayak','Girish','Aarti','Carol','Wong']
print("Index: 1=Add\n 2=Remove\n 3=Count\n 4=Display book\n")
choice=1
while choice>0 and choice<=4:
    choice = int(input("Enter a menu choice:"))
    if choice==1:
        x=input("Enter your name:")
        l1.append(x)
        print("List updated....New student added.")

    elif choice==2:
        y=input("Enter your name: ")
        l1.remove(y)
        print("List updated.....Entry deleted!")
    elif choice==3:
        print("There are ",len(l1),"Students in List.")

    elif choice==4:
        print("Sorted List is:")
        print("Name")
        l1.sort()
        print(l1)
    else:
        print("Invalid Choice....Closing Application")
