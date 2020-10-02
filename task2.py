#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
a=input("enter in your number").strip()
a=float(a)
a = round(a,3)
b=a**(1.0/3.)
b = round(b,3)
c=a**(1.0/2.)

b=float(b)
number1=int(b)

c=float(c)
number2=int(c)



if c==number2 and b==number1:
    print( str(a)+ " is both a perfect square and a perfect cube")
elif c==number2:
    print( str(a)+ " is only a perfect square")
elif b==number1:
    print(str(a)+ " is only a perfect cube")
