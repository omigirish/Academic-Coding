x=int(input("Enter number of rows u need: "))
for i in range(1,x+1,1):
    for k in range(1,50-2*i):
        print(end=' ')
    for j in range(1,i,1):
        print("*",end='   ')
    print("\n")