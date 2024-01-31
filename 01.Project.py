#coded by Asa Whitman
import math
x = int(input("Enter length of time in days: "))
Years = x // 365
print("Years: ",Years)
x -= (Years * 365)
Weeks = x // 7
print("Weeks: ",Weeks)
x-= (Weeks * 7)
print("Days: ",x)