# THIS IS THE MAIN FILE FOR HOMEWORK 4
# This program reads a file of member information and writes a file of member information to a csv file
# It also formats the date with slashes and calculates the membership fee

# Import the necessary modules
try:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib"))) 
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "classes")))

    import filelib
    import member
   
except ModuleNotFoundError as e:
    print(
        f"{e}! Please ensure the module is named correctly and either:\n"
        "  - In the same directory as this program, or\n"
        "  - In the 'lib' or 'classes' folder one level above this program's directory.\n"
        "To use my file system setup, download it from: https://github.com/jfar5522/python-class-2025")
    sys.exit(f"Import failure! {e} available!")

# This is the main function for the program
def main(): 

    # This is the function that writes the input file to the input.txt file
    filelib.fileWriter("input.txt", "CID|NAME|EMAIL|MEMBERSHIP_START|MEMBERSHIP_TYPE|SIGNUPFEE|FIRSTTIME|MEMBERSHIP_FEE\n" 
    "83947|MARK L. PHILLIPS|mphilips@gmail.com|11-21-23|1|70|1|120\n"
    "76856|ALICE B. WILSON|wila125@gmail.com|10-10-21|2|48|0|1200\n"
    "64787|CHRISTIE C. MOORE|c.moore87@comcast.com|09-01-20|2|45|1|1200\n"
    "57652|RICHIE S. EGGLESTON|seggle@aol.com|09-01-20|1|45|0|120", 1, True)

    # print(filelib.fileReader("input.txt"))

    # This is the list that will contain the member objects
    memberList = []

    # This is the input file for the program
    input = filelib.fileReader("input.txt")
    
    # This is the loop that reads the input file and creates the member objects
    for line in input:
        data = line.split("|")
        cid = data[0]
        name = data[1]
        email = data[2]
        membership_start = data[3]
        membership_type = data[4]
        signupfee = data[5]
        firsttime = data[6]
        membership_fee = data[7]

        # This is the loop that creates the member objects
        if membership_type == "1":
            monthlyMember = member.MonthlyMember(cid, name, email, membership_start, signupfee, firsttime, membership_fee)
            memberList.append(monthlyMember)
        elif membership_type == "2":
            yearlyMember = member.YearlyMember(cid, name, email, membership_start, signupfee, firsttime, membership_fee)
            memberList.append(yearlyMember)
        else:
            if membership_type == "MEMBERSHIP_TYPE":
                columnNames = member.Member(cid, name, email, membership_start, signupfee, firsttime, membership_fee)
                memberList.append(columnNames)
                continue
            else:
                raise ValueError("Invalid membership type! Make sure to use either 1 or 2 for the membership type.")

    # This is the loop that formats the date with slashes and calculates the membership fee
    for m in memberList:
        m.formatDateWithSlashes()
        print(m.getMembershipFee())

    # This is the function that writes the member objects to a csv file 
    filelib.fileWriter("members.csv",memberList)


main()

    
    
