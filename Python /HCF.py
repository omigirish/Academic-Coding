def HCF(x,y):
    hcf=-1
    if x>y:
        t=x
    else:
        t=y
    for i in range((t+1),1,-1):
        if x%i==0 and y%i==0:
            hcf=i
            break

        else:
            pass
    if hcf==-1:
        hcf=1
    return hcf

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("HCF of the two numbers is: ",HCF(x=a,y=b))
