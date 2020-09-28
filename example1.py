#! python3

"""
Examples showing how logical operators can be used:
There are two important logical operators:
1. and - all of the conditions must evaluate to be true
2. or - at least one of the conditions must evaluate to be true
"""

print("=======================================")
print(" Example 1: and statements             ")
a = 5
b = 10
if a==5 and b==10:
  print("Both statements are true")
else:
  print("At least one statement is false")
print("=======================================")

print("\n\n\n")

print("=======================================")
print(" Example 2: or statements             ")
a = 5
b = 10
c = 2
if a==5 or b==10 or c==0:
  print("At least one statement is true")
else:
  print("All statements must be false")
print("=======================================")
