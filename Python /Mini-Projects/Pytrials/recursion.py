def fact(no):
    if no<=1:       # exit condition to terminate the function calls
        return 1
    else:
        return no*fact(no-1)
no=int(input("enter the number"))

#function call with given value as the argument
print("factorial of given number is =",fact(no))