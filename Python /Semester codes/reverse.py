str=input("Enter a string: ")
x=len(str)
l1=list(str)
for i in range((x-1),-1,-1):
    print(l1[i],end='')