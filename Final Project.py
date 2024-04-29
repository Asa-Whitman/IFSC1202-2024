#Coded by Asa Whitman
class user ():
    def __init__(self, username, password):
        self.username = username
        self.password = password
class userlist ():
    def __init__(self, filename):
        self.filename = filename
        self.Ulist = []
    
    def ReadUserFile(self):
        passwordsfile = open(self.filename)
        list = passwordsfile.readline().replace("\n","")
        while list != "":
            line = list.split(",")
            myuser = user(line[0],line[1])
            self.Ulist.append(myuser)
            list = passwordsfile.readline().replace("\n","")
        passwordsfile.close()      
    
    def WriteUserFile(self):
        passwordsfile = open(self.filename,"w")
        for i in range (len(self.Ulist)):
            passwordsfile.write(self.Ulist[i].username + "," + self.Ulist[i].password + "\n")
        passwordsfile.close()
    
    def DisplayUserList(self):
        print(("{:16s}{:16s}".format("Username", "Password")))
        print("--------------- ---------------")
        for i in range (len(self.Ulist)):
            print("{:16s}{:16s}".format(self.Ulist[i].username, self.Ulist[i].password))
    
    def FindUserName(self, username):
        for i in range (len(self.Ulist)):
            if self.Ulist[i].username == username:
                return i
        return -1
    
    def ChangePassword(self, username):
        index = myuserlist.FindUserName(username)
        if index != -1:
            newpass = str(input("Enter new password: "))
            passapprove = 0
            while passapprove == 0:
                for i in range (len(self.Ulist)):
                    self.Ulist[index].password = newpass
                    passcheck = myuserlist.Strength(newpass)
                if passcheck == 5:
                    print("password changed")
                    passapprove += 1
                else:
                    print("password is too weak -",passcheck)
                    newpass = str(input("Enter a stronger password: "))
        else:
            print("User not found")
    
    def AddUser(self, username, password):
        index = myuserlist.FindUserName(username)
        if index != -1:
            print("User already exists")
        else:
            myuser = user(username, password)
            self.Ulist.append(myuser)
            newpass = self.Ulist[index].password
            passapprove = 0
            while passapprove == 0:
                for i in range (len(self.Ulist)):
                    self.Ulist[index].password = newpass
                    passcheck = myuserlist.Strength(newpass)
                    if passcheck == 5:
                        passapprove += 1
                    else:
                        print("password is too weak -",passcheck)
                        newpass = str(input("Enter a stronger password: "))
            print("User added.")
    
    def DeleteUser(self, username):
        index = myuserlist.FindUserName(username)
        if index != -1:
            del self.Ulist[index]
            print("User deleted.")
        else:
            print("User not found")
    
    def Strength(self, password):
        SpecialChar = "~!@#$%^&*()_+|-={}[]:;<>?/"
        haslower = 0
        hasupper = 0
        hasnum = 0
        hasspecial = 0
        haseight = 0
        for i in range (0, len(password)):
            if password[i].islower():
                haslower = 1
            elif password[i].isupper():
                hasupper = 1
            elif password[i].isdigit():
                hasnum = 1
            elif password[i] in SpecialChar:
                hasspecial = 1
        if len(password) >= 8:
            haseight = 1
        score = haslower + hasupper + hasnum + hasspecial + haseight
        return score
        
myuserlist = userlist("Final Project Passwords.txt")
myuserlist.ReadUserFile()
i=0
while i != 6:
    Input = int(input("1) Add a New User\n2) Delete an Existing User\n3) Change Password on an Existing User\n4) Display All Users\n5) Save Changes to File\n6) Quit\n\nEnter Selection: "))
    if Input < 1 or Input > 6:
        Input = int(input("Bad selection. Please enter a valid selection: "))
    elif Input == 1:
        inputuser = str(input("Enter Username: "))
        inputpass = str(input("Enter Password: "))
        myuserlist.AddUser(inputuser, inputpass)
    elif Input == 2:
        inputuser = str(input("Enter username: "))
        myuserlist.DeleteUser(inputuser)
    elif Input == 3:
        inputuser = str(input("Enter your username: "))
        myuserlist.ChangePassword(inputuser)
    elif Input == 4:
        myuserlist.DisplayUserList()
    elif Input == 5:
        myuserlist.WriteUserFile()
        print("File saved")
    elif Input == 6:
        print("closing program")
        i = 6
        break