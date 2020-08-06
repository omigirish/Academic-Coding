
def temp_convert(hi=0):#here function has default argument
    far=hi*(9/5)+ 32
    return far


hi=int(input("enter the temperature in degrees"))

    #function call with given temperature as the argument
print("corresponding temperature in farenhite is {0}".format(temp_convert(hi)))

    #function call when functon has no arguments,function will take the default value(that is 0(zero)) for
                                                #converting the  temperature into farenhite
print("value of 0 degree celcius in farenhite is = {0}".format(temp_convert()))

