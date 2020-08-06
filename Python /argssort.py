def sorter(*args):
    l=list(args)
    for i in range(0,len(l)):
        for j in range(0,len(l)-1):
            if l[j]>=l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp

    print(l)

sorter(10.15,23,7,1,6,45,0)