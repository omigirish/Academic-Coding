'''n=int(input("How many numbers are u going to enter?"))
l=[]
for i in range(n):
    l+=[int(input("enter no: "))]
s=0
for i in range(n):
    s=s+l[i]
    l[i]=s
print(l)
print(l[-2])
del l[-2]
print(l+l)
print("Value of a is %i %i %i"%(10,20,30))
a=10
b=20
print(f"Value of a is {a} and b is {b}")
print("Value of a is {0}".format(a))'''
l1=[10,20,30,40,20,20,20]
print(l1[1:10:])
l2=list(reversed(l1))
print(l2)
while 20 in l1:

    l1.remove(20)
print(l1)
l1.insert(2,"helO")
print(l1)
t1=tuple(l1)
print(t1)
l3=list(t1)
print(l3)

