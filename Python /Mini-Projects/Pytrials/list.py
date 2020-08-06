s=""
s = raw_input("Enter a string: ")
a = s.split(" ")
print(a)
t = tuple(a)


print("Tuples are: ")
print(t)


option = 0


while (option !=4):
    print("Choose an option:")

    print("1. Display the total number of tuples")
    print("2. Print a sub tuple using slicing operation")
    print("3. Find whether a given word is available in the tuple or not")
    print("4. EXIT")

    option = int(input())

    if (option == 1):
        length = len(t)
        print("Total number of tuples = ", length)


    elif (option == 2):
        a = int(input("Enter start of sub tuple: "))
        b = int(input("Enter end of sub tuple: "))
        c = int(input("Enter step size of sub tuple: "))
        print("The sub tuple is: ")
        for i in range(a,b,c):
            print(t[i])

    elif (option == 3):
        word = input("Enter the word to be searched for: ")
        if word in t:
            print("Word was found")
        else:
            print("Word was not found")

    elif(option == 4):
        print("Exit successful")
        break
    else:
        print("Invalid Input")
