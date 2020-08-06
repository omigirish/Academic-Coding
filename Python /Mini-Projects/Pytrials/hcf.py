def hcf(x,y):
    if x>y:      #finding the smaller number between given
        smaller=y               #two numbers
    else:
        smaller=x

    for i in range(1,smaller+1,1):
        if (x%i==0 and y%i==0):
            hcf=i
    return hcf

a=int(input("enter the first number="))
b=int(input("enter the second number="))
hh=hcf(y=b,x=a)     #calling the function with keyword arguments
print("HCF of given numbers is =",hh)
