height=() #CREATING EMPTY TUPLE
c=0
while(c==0):

    print("1 for adding  new height\n2 for displaying maximum and minimum height\n3 for dislaying average height\n4 for dislaying height of students in ascending order")
    n = int(input("Enter value:"))
    if (n == 1):
        a = input("Enter height:")
        height=height+(a,) #ADDING NEW HEIGHT INTO THE TUPLE
    elif(n==2):
        print("Maximum height is",max(height))#PRINTING MAXIMUM HEIGHT OF THE TUPLE
        print("Minimum height is",min(height))#PRINTING MINIMUM HEIGHT OF THE TUPLE

    elif(n==3):

        sum=0
        for i in height:
            sum=sum+int(i)

        print("Average height: %f"%(sum/int(len(height))))#PRINTING THE AVERAGE HEIGHT OF THE TUPLE
    elif(n==4):
        print(sorted(height))#PRINTING THE HEIGHT IN ASCENDING ORDER
    else:
        print("Invalid input")
