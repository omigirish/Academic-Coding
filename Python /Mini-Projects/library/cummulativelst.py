'''Write a function that takes a list of numbers as input from the
user and produces the corresponding cumulative list where each element
in the list at index i is the sum of elements at index j<=i'''

no=int(input("How many numbers are u going to enter?"))
x=0
l=list()
while x<no:
    n=int(input("Enter a number:"))
    l.append(n)
    x+=1
    print(x)

def getClist(lst):
    clist=list()
    for index,value in enumerate(lst):
        if index==0:
            clist.append(value)
        else:
            clist.append(clist[index-1]+lst[index])

    return clist
print(f"Orignal list is:      {l}")
print(f"Cummulative List is : {getClist(l)}")
