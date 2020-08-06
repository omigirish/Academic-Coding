
class ValueError(Exception):
    pass


class NotFound(Exception):
    pass

def add(l1):
    fl=0
    name=input("Enter name: ")
    month=input("Enter month: ")
    consumption=int(input("Enter electricity consumption: "))
    t1=(name,month,consumption)
    try:
        if consumption < 0:
            raise ValueError
        else:
            l1.append(t1)
            print(l1)
    except ValueError:
            print("Value not accepted!")

    return l1

def delete(l1):
    fl=0
    name=input("Enter name of the user whose record you want to delete: ")
    month=input("Enter month in which record has to be deleted: ")
    for i in l1:
        if name in i:
            if month in i:
                l1.remove(i)
                fl=1
    try:
        # noinspection PyUnreachableCode
        if fl==0:
            raise NotFound
        else:
            print(l1)

    except NotFound:
            print("Data not found!")


    return l1

def update(l1):
    fl=0
    name=input("Enter the name of the user whose consumption is to be updated: ")
    month=input("Enter the month of the user whose consumption is to be updated: ")
    consumption=int(input("Enter consumption value to be updated: "))
    for i in l1:
        if name in i:
            if month in i:
                l1.remove(i)
                t1=(name,month,consumption)
                l1.append(t1)
                fl=1
    try:
        if fl==0:
            raise NotFound
        else:
            print(l1)
    except NotFound:
        print("Data not found!")
    return l1


def display(l1):
    for i in l1:
        print(i)

def average(name,l1):
    sum=0
    c=0
    for i in l1:
        if name in i:
            sum=sum+int(i[2])
            c=c+1

    print("Average=",sum/c)








l1=[('Janhavi','December',600)]
choice=0
while (choice!=6):
    choice=int(input("Select one of the following options: \n1.Add a new record.\n2.Modify existing record.\n3.Delete record. \n4.Print Record. \n5.Average\n6.Exit\n"))

    if(choice == 1):
        add(l1)
    elif (choice == 2):
        update(l1)
    elif (choice == 3):
        print(l1)
        delete(l1)
    elif (choice == 4):
        display(l1)
    elif(choice==5):
        name=input("Enter name:")
        average(name,l1)
    else:
        print("Bye!")
        break

