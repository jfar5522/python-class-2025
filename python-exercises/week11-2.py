class Animal:
    age=2
    weight=1
    color=1
    height=52
    def growAndMature(self):
        print("Animal grows bigger")
        self.height += 1
        print("Animal will age a bit more")
        self.age += 1

bigdog=Animal()
bigdog.height=90
smalldog=Animal()
smalldog.height=10


class Student:
    UID = ""
    firstName = ""
    lastName = ""
    DOB = ""
    diploma = "no"
    def __init__(self,fname,lname):
        # self.UID=uid
        self.firstName=fname
        self.lastName=lname
        # self.DOB=dob
    def finishCollege(self):
        self.diploma="yes"

# bob=Student()
# bob.UID = "U1234567"
# bob.firstName= "Bob"
# bob.lastName= "Jones"
# bob.DOB= "07/15/2002"

# lisa=Student()
# lisa.UID= "U2345678"
# lisa.firstName= "Lisa"
# lisa.lastName= "Simpson"
# lisa.DOB= "05/14/1997"

# christie=Student()
# christie.UID= "U3456789"
# christie.firstName = "Christie"
# christie.lastName ="Smith"
# christie.DOB ="08/17/2004"

bob=Student("Bob","Jones",)
lisa=Student("Lisa","Simpson",)
christie=Student("Christie","Smith",)

bob.finishCollege()
lisa.finishCollege()
christie.finishCollege()

# print(bob.diploma)




