#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
a=input("an integer ")
b=input("an integer ")
a=int(a)
b=int(b)
if a>b: 
    number1=a%b
    if number1==0:
        print(str(b)+" is a factor of " +str(a))
    else:
        print(str(b)+" is not a factor of "+str(a))

elif a<b:
    number2=b%a
    if number2==0:
        print(str(a) +" is a factor of a "+str(b))
    else:
        print(str(a)+" is not a factor of a "+str(b))
