#coded by Asa Whitman
Start = int(input("enter start of range: "))
End = int(input("enter end of range: "))
print("Special numbers between {} and {}:".format(Start, End))
while Start <= End:
    Answer = 0
    DigitAmount = 0
    i = Start
    while i != 0:
        i //= 10
        DigitAmount += 1
    Sum = 0
    x = Start
    while x != 0:
        Digit = x % 10
        Sum += Digit
        Product = Sum ** DigitAmount
        Answer += Product
        Sum = 0
        x //= 10
    if Answer == Start:
        print(Start)
    Start += 1