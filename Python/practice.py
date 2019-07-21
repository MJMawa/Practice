from math import *
operator = input("Enter operation---> *, +, - , /, **  ")

if operator == "+":
    num = input("How many numbers are you adding? ")
    my_num = list()
    i = 1
    while int(num) >= i:
        print("Enter number ", i)
        my = int(input())
        my_num.append(my)
        i += 1
    print("Total = ", sum(my_num))
elif operator == "**":
    base = int(input("Enter base:  "))
    exp = int(input("Enter power:   "))
    print("%d^%d = %s"%(base, exp, str(pow(base, exp))))
    
        
