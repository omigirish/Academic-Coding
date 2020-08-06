def reverse(ii):
    i=len(ii)
    j=""
    for i in range(i-1,-1,-1):
        j=j+ii[i]
    return j


print("reversed string is =", reverse(input("enter the string=")))