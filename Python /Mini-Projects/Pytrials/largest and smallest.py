l1=[]
for i in range(4):
    x=int(input("Enter number:"))
    l1.append(x)

l1.sort()
print(l1)
print("Smallest number is ",l1[0])
print("Largest number is ",l1[3])