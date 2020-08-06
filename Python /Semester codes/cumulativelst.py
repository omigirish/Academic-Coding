'''Write a function that takes a list of numbers as input from the
user and produces the corresponding cumulative list where each element
in the list at index i is the sum of elements at index j<=i'''

no=input("How many numbers are u going to enter?")
x=1
l=list()
while x<no :
    n=int(input("Enter a number:"))
    print(x+1)
    l[x]=n
    ++x

def getClist(lst):
    clist=list()
    for x in enumerate(lst):
        if x==0:
            pass
        else:
            clist[x]=lst[x]+lst[x-1]

    return clist

print(getClist(l))
