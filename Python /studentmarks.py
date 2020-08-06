def result(x):
    sum = 0
    for i in x.values():
        sum=sum+i
    average=sum/len(x)
    print("Average marks obtained by Students is:")
