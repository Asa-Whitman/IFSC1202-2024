#coded by Asa Whitman
a = []
b = []
propertieslist = open("Exam Two Properties.csv")
x = propertieslist.readline().replace("\n","")
while x != "":
    x = x.split(",")
    a.append(x)
    x = propertieslist.readline().replace("\n","")
for i in range(len(a)):
    for j in range(len(b)):
        if a[i][3] == b[j][0]:
            b[j][1] = b[j][1] + 1
            b[j][2] = b[j][2] + int(a[i][4])
            break
    else:
        b.append([a[i][3],1, int(a[i][4])])
print("Zipcode Count Average")
for z in range(len(b)):
    print(b[z][0],b[z][1],"$",round(b[z][2]/b[z][1],2))