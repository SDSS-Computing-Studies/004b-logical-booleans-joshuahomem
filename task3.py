#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
a=input("enter in any number")
a=float(a)
if a>0:
    print(str(a)+" is a posotive integer")
elif a<0:
    print(str(a)+" is not a posotive integer")
