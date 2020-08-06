n=int(input("How many numbers are u going to enter?"))
l=[]
for i in range(n):
    l.append(int(input("enter no: ")))
s=0
for i in range(n):
    s=s+l[i]
    l[i]=s
print(l)