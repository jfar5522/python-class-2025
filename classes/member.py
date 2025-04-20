# Member class
# This class is the parent class for the MonthlyMember and YearlyMember classes
# It contains the common attributes and methods for the two classes
class Member:
    def __init__(self, cid, name, email, membership_start, signupfee, firsttime, membership_fee):
        self._cid = cid # customer id
        self._name = name # name of the member
        self._email = email # email of the member
        self._membershipStart = membership_start # date of membership start
        self._signupFee = signupfee # starting fee for the membership
        self._firstTime = firsttime # 0 = not first time, 1 = first time
        self._membershipFee = membership_fee # membership fee

    # string representation of the member
    def __str__(self): 
        return f"{self._cid},{self._name},{self._email},{self._membershipStart},{self._membershipFee}"
    
    # getters and setters for the member attributes
    @property
    def cid(self):
        return self._cid
    @cid.setter
    def cid(self, cid):
        self._cid = cid
    
    @property
    def name(self):
        return self._name    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def membershipStart(self):
        return self._membershipStart
    @membershipStart.setter
    def membershipStart(self, membershipStart):
        self._membershipStart = membershipStart

    @property
    def signupFee(self):
        return self._signupFee
    @signupFee.setter
    def signupFee(self, signupFee):
        self._signupFee = signupFee

    @property
    def firstTime(self):
        return self._firstTime
    @firstTime.setter
    def firstTime(self, firstTime):
        self._firstTime = firstTime

    @property
    def membershipFee(self):
        return self._membershipFee
    @membershipFee.setter
    def membershipFee(self, membershipFee):
        self._membershipFee = membershipFee

    # gets the membership fee   
    def getMembershipFee(self):
        fee = 0
        membershipType = self.__class__.__name__

        # if the member is a first time member, add the signup fee to the fee variable
        if self._firstTime == "1":
            fee = int(self._signupFee)
        elif self._firstTime == "0":
            fee = 0
        elif self._firstTime == "FIRSTTIME":
            return "Total Membership Fees:"
        else:
            raise ValueError("Invalid first time value! Make sure to use either 1 or FIRSTTIME for the first time value.")

        # adds the membership fee to the fee variable
        if membershipType == "MonthlyMember":
            fee += 120
        elif membershipType == "YearlyMember":
            fee += 1200
        else:
            raise ValueError("Invalid membership type! Make sure to name the member class as MonthlyMember or YearlyMember")
            
        return fee
    
    # formats the date with slashes
    def formatDateWithSlashes(self):
        if self.membershipStart == "MEMBERSHIP_START":
            return None
        else:
            try:
                self.membershipStart.replace("-", "/")
            except ValueError:
                raise ValueError("Invalid membership start date! Make sure to use the format MM-DD-YYYY for the membership start date.")

    
# Monthly Member Class
class MonthlyMember(Member): 
    def __init__(self, cid, name, email, membership_start, signupfee, firsttime, membership_fee):
        super().__init__(cid, name, email, membership_start, signupfee, firsttime, membership_fee)
    def __list__(self):
        return [self._cid, self._name, self._email, self._membershipStart, self._firstTime, self._membershipFee]

# Yearly Member Class
class YearlyMember(Member):
    def __init__(self, cid, name, email, membership_start, signupfee, firsttime, membership_fee):
        super().__init__(cid, name, email, membership_start, signupfee, firsttime, membership_fee)
    def __list__(self):
        return [self._cid, self._name, self._email, self._membershipStart, self._firstTime, self._membershipFee]





