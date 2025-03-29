#THIS IS THE "MAIN" FILE!
#Got bugs? Please let me know!

#import function modules from the "lib" folder
try:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib")))

    import filelib

except ModuleNotFoundError: 
    #You aren't using my file system, so make sure the module file is in the same place as this program!
    #To run this program with my file system in mind download it here on my github! https://github.com/jfar5522/python    
    import filelib

#import class modules from the "classes" folder
try:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "classes")))

    import customer

except ModuleNotFoundError: 
    import customer

#write input file demonstration and eventual execution

#manual (harder) way of writing with function as an example of not needing to use lists. (aka why you should use lists because they're great)
# filelib.fileWriter("input.txt","",0,1)
# filelib.fileWriter("input.txt","Account#:Amount",1)
# filelib.fileWriter("input.txt","42-8798:125988.87",2)
# filelib.fileWriter("input.txt","78-6746:43762.18",3)
# filelib.fileWriter("input.txt","34-1245:1243.21",4)
# filelib.fileWriter("input.txt","91-7483:13337.73",5)

#medium level way of doing it, easier but not the most efficent or useful way to write
# filelib.fileWriter("input.txt","Account#:Amount\n42-8798:125988.87\n78-6746:43762.18\n34-1245:1243.21\n91-7483:13337.73",1,1)

#easiest and best way to write using a list, no I have not made it compatiable to write a dictionary out.
filelib.fileWriter("input.txt",["Account#:Amount","42-8798:125988.87","78-6746:43762.18","34-1245:1243.21","91-7483:13337.73"])

#assigns lineList a list of each line from the input.txt file
lineList = filelib.fileReader("input.txt",1)

# goes through the file's line list, splits each line at the ":" and then assigns accountNum to the first half and amount to the 
# other half. Finally creates a list which appends a new customer object with the accountnum and amount as attributes.
# Who needs dictionaries am I right?
customerList = []
for line in lineList:
    line = str(line)
    lineSplit = line.split(":")
    accountNum = lineSplit[0]
    amount = lineSplit[1]

    customerList.append(customer.Customer(accountNum, amount))

print(customerList)

# goes through the customer object list and runs the "calcuateInterestPayment" customer class function which in turn
# takes the percentage of the account amount and adds that percentage to the account's amount
for act in customerList:
    act.calculateInterestPayment(5)

    print(act._amount)

#takes the customer list and outputs it to the output.csv file
filelib.fileWriter("output.csv",customerList)




