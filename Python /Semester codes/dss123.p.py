def max(a,b,c):
    largest = 0
    if(a>b) and (a>c):
        largest = a
    elif(b>c) and (b>a):
        largest = b
    elif (c>a) and (c>b):
        largest = c
    return largest
a=int(input("Enter first value"))
b=int(input("Enter second value"))
c=int(input("Enter third value"))
d=max(a,b,c)
print(d)