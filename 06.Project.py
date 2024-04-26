#coded by Asa Whitman
outputfile = open("06.Project Output File.txt","w")
inputfile = open("06.Project Input File.txt","r")
mergefile = open("06.Project Merge File.txt","r")
input = inputfile.readline()
merge = mergefile.readline()
inrecord = 0
mergerecord = 0
outrecord = 0
while input != "":
    if input == "**Insert Merge File Here**\n":
        while merge != "":
            outputfile.write(merge)
            mergerecord +=1
            merge = mergefile.readline()
            outrecord +=1
        if merge =="":
            outputfile.write("\n")
            mergefile.close()
    if input != "**Insert Merge File Here**\n":
         outputfile.write(input)
         outrecord += 1
         inrecord +=1
    input = inputfile.readline()
print(inrecord, "input file records")
print(mergerecord, "merge file records")
print(outrecord, "output file records")

outputfile.close()
inputfile.close()