#coded by Asa Whitman
Start = int(input("Enter start of range: "))
End = int(input("Enter end of range: "))
print("Prime numbers between {} and {}:".format(Start, End))
for i in range(Start, End+1):
    if i>1:        
        for j in range(2, (i//2)+1):
            if (i % j) == 0:
                break
        else:
            print(i)