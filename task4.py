#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

VIPNames = ("Guile","Blanka","Christine","Carol","Richard","Daniel","Chun-Li")
a=input("enter in your name ").strip()
if "Guile"in a or"Blanka"in a or"Christine"in a or"Carol"in a or"Richard"in a or"Daniel"in a or"Chun-Li" in a:
    print("Hi " +a+"! you are a VIP!")
else:
    print("You are not a vip")
