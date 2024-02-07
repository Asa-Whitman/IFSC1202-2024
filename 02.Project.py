#coded by Asa Whitman
import math
SideOne = float(input("Enter side one: "))
SideTwo = float(input("Enter side two: "))
SideThree = float(input("Enter side three: "))
s = SideOne + SideTwo + SideThree
s /= 2

A = math.sqrt(s * (s - SideOne) * (s - SideTwo) * (s - SideThree))
print("Triangle Area: ", A, " square units.")