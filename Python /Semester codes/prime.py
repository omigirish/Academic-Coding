n=int(input("Enter n"))
print("2")
for i in range(1,n+1):
    for j in range(2,i):
        if i%j==0:
            break
        if i-1==j:
            print("%i"%i)