n = int(input("Enter the number of names: "))
l1=[]
for i in range(1,n+1,1) :
    name = input("Enter name: ")
    l1.append(name)
print (l1)

choice = int(input("Select your choice"))

while(choice!=5) :

    print ("1. Add a student name")
    print ("2. Delete a given student")
    print ("3. Display total count of students")
    print ("4. Print the student list in ascending order")
    print ("5. Exit")

    choice = int(input("Select your choice"))


    if(choice==1):
        name=input("Enter name to be added")
        l1.append(name)
    elif(choice==2) :
        name=input("Enter name to be deleted")
        l1.remove(name)
    elif(choice==3) :
        print("Total count of students = ",len(l1))
    elif(choice==4) :
        l1.sort()
        print("Sorted student list =",l1)
    else :
          break


