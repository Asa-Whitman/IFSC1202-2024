#coded by Asa Whitman
import math
x = float(input("Enter first number: "))
Opsign = str(input("Enter Operator (+,-.*,/): "))
y = float(input("Enter second number: "))
if Opsign == "+":
    print (x + y)
elif Opsign == "-":
    print (x - y)
elif Opsign == "*":
    print (x * y)
elif Opsign == "/":
    print (x / y)
else:
    print("Invalid Operator!")