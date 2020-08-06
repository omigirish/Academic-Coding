def sorted_order(*args):
    ll=[]
    for num in args: #for copying the numbers in args to list for sorting them
        ll.append(num)
    for i in range(0,len(args)):#for loop to sort the numers passed to the function
        for j in range(0,len(args)-1):
            if ll[j]>ll[j+1]:
                temp=ll[j]
                ll[j]=ll[j+1]
                ll[j+1]=temp
    return ll
#first function call is with 10,20,30,56,3 numbers as arguments and return the sorted order of the numbers

print("sorted order of the given numbers 10,20,30,56,3 is ",sorted_order(10,20,30,56,3))

#second function call is with different number of arguments and sort the numbers

print("sorted order of the given numbers 678,200,-30 is ",sorted_order(200,678,-30))
