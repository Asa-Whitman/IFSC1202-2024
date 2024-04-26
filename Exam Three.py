#coded by Asa Whitman
import math
class Triangle ():
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    def Type(self):
        if self.s1 == self.s2 and self.s1 == self.s3:
            type = "Equilateral"
            return type
        elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
            type = "Isoceles"
            return type
        else:
            type = "Scalene"
            return type
    def Perimeter(self):
        perimeter = self.s1 + self.s2 +self.s3
        return perimeter
    def Area(self):
        s = self.s1 + self.s2 +self.s3
        s /= 2
        area = math.sqrt(s(s - self.s1)*(s-self.s2)*(s-self.s3))
        return area
    def Angle1(self):
        angle1 = math.acos(((self.s2**2) + (self.s3**2) - (self.s1**2)) / (2*self.s2*self.s3)) * (180/math.pi)
        return angle1
    def Angle2(self):
        angle2 = math.acos(((self.s3**2) + (self.s1**2) - (self.s2**2)) / (2*self.s3*self.s1)) * (180/math.pi)
        return angle2
    def Angle3(self):
        angle3 = math.acos(((self.s1**2) + (self.s2**2) - (self.s3**2)) / (2*self.s1*self.s2)) * (180/math.pi)
        return angle3
    
def print_trianglelist(Trianglelist):
	print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format("Type", "Side 1", "Side 2", "Side 3", "Perimeter", "Area", "Angle 1", "Angle 2", "Angle 3"))
	for i in range(len(Trianglelist)):
		print ("{:>14s}{:14.2f}{:14.2f}{:14.2f}{:14.2f}{:14.2f}{:14.2f}{:14.2f}{:14.2f}".format(Trianglelist[i].Type, Trianglelist[i].s1, Trianglelist[i].s2, Trianglelist[i].s3(), Trianglelist[i].Perimeter(), Trianglelist[i].Area(), Trianglelist[i].Angle1(), Trianglelist[i].Angle2(), Trianglelist[i].Angle3()))

def find_tri(Trianglelist,tritofind)
     for i in range(len(Trianglelist)):
        if Trianglelist[i].Type == tritofind:
            return i
        return -1		

File = open("Exam Three Triangles.txt")
x = File.readline().replace("\n","")

a=[]
Trianglelist=[]

while x != "":
    y = x.split(",")
    mytriangle = Triangle(y[0].strip(), float(y[1].strip()), float(y[2].strip()))
    Trianglelist.append(mytriangle)
    x = File.readline().replace("\n","")

print("Type    Side 1     Side 2     Side 3     Perimeter     Area     Angle 1     Angle 2     Angle 3")
