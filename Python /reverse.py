def rev(str):
    x=len(str)
    l1=list(str)
    l2=""
    for i in range((x-1),-1,-1):
        l2=l2+l1[i]
    return l2

str=input("Enter a string: ")
l=""
l=rev(str)
print("The reversed String is: ",end='')
print(l)
