#coded by Asa Whitman
import requests
constitution = requests.get('https://www.usconstitution.net/const.txt')
filestring = constitution.text
filestringlist =filestring.split("\n")
searchterm = input("Enter search term: ")
start = 0
end = 0
while searchterm != "":
    for i in range(len(filestringlist)):
        pos = filestringlist[i].find(searchterm)
        if pos != -1:
            for j in range(i,0,-1):
                if filestringlist[j] == "":
                    start=j
                    break
            for k in range(i,len(filestringlist)):
                if filestringlist[k] == "":
                    end=k
                    break
            for m in range(start, end):
                print("Line",m,":",filestringlist[m])
        i = end
    searchterm = input("enter another search term (leave blank to end program): ")