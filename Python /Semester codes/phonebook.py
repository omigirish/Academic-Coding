phonebook={222:'girish',666:'sushant',777:'chiren'}
yes=1
print(phonebook)
while yes==1:
    print('press 1 to add new entry \npress 2 to remove the entry \npress 3 to display phonebook when key is given\npress 4 to display the phonebook in sorted order according to value\npress 5 to display the phonebbok in sorted order according to keys')

    choice=int(input("enter your choice="))
    if choice==1:
        name=input("enter the name")
        no=int(input("enter the phone number"))
        phonebook.update({no:name})
        print("phonebook updated")
        print(phonebook)
    elif choice==2:
        no=int(input("enter the phone number which has to be deleted="))
        del phonebook[no]
        print("phonebook updated")
        print(phonebook)
    elif choice==3:
        no=int(input("enter the key value for which the value to be displyed="))
        print("corresponding value of key is={0}".format(phonebook[no]))
    elif choice==4:
        print("displaying the list in sorted order accordinng to the values=")
        print("number \t name")
       # l1=list(phonebook.values())
        for key,value in sorted(phonebook.items(),key=lambda x:x[1]):
            print("{0}\t {1}".format(key,value))
    elif choice==5:
        print("displaying the the list according to the keys=")
        l1=list(phonebook)
        l1.sort()
        print("number\t name")
        for i in l1:
            print(i,"\t",phonebook[i])
    yes = int(input("enter 1 to contine and 0 to stop"))
