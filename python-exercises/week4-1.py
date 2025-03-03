
#creates and assigns the following varibles to a user input.
studentName = input("Enter student's name:")
major = input("Enter student's major:")

#if major starts with a vowel, print statement with user input with "an" before major, else print with "a". The "a" bugged me. Also prints message about major.
if major[0].lower() in {"a", "e", "i", "o", "u", "y"}:
    print("Hello, my name is %s and I am an %s student"%(studentName, major))
else:
    print("Hello, my name is %s and I am a %s student"%(studentName, major))
print('''The major you selected will be a challenge to complete.''')

#prints out a statement which then uses the \n enter key to print multiple lines.
print("Hey %s,\nfor the major %s you must\nremember to pay your student tuition."%(studentName, major))

#creates an array of names that asks the user to input names for each array value.
names = []
name1 = input("Enter a first name:")
name2 = input("Enter a second name:")
name3 = input("Enter a third name:")
names.append(name1)
names.append(name2)
names.append(name3)
print(names)


#creates the student records dictionary then creates 3 student record arrarys containing UID, first and last name, and major which are then added to the student records dictionary 1 at a time. Finally it prints out the student records dictionary
studentRecords = {}
UID1 = input("Please insert first student's UID:")
sFirst1 = input("Please insert first student's first name:")
sLast1 = input("Please insert first student's last name:")
major1 = input("Please insert first student's major:")
record1 = [UID1, sFirst1, sLast1, major1]
studentRecords.update({UID1:record1})

UID2 = input("Please insert second student's UID:")
sFirst2 = input("Please insert second student's first name:")
sLast2 = input("Please insert second student's last name:")
major2 = input("Please insert second student's major:")
record2 = [UID2, sFirst2, sLast2, major2]
studentRecords.update({UID2:record2})

UID3 = input("Please insert third student's UID:")
sFirst3 = input("Please insert third student's first name:")
sLast3 = input("Please insert third student's last name:")
major3 = input("Please insert third student's major:")
record3 = [UID3, sFirst3, sLast3, major3]
studentRecords.update({UID3:record3})

print(studentRecords)

''' OLD ORIGINAL WAY I DID THE LOOKUP
print("\nWelcome to the UID lookup!\nPlease insert a valid UID to search for.\nOtherwise to quit the program please type 'exit'.\n")
exit = 0
while exit == 0:
    searchedID = input("Enter a student UID:")
    if searchedID.lower() in {"exit", "quit"}:
        exit = 1
        continue
    elif searchedID in studentRecords:
            print(f"Here are the student records associated with the UID '{searchedID}' ordered ID, first name, second name, and major:\n{studentRecords[searchedID]}\nIf you want to search another id please enter in a new id.\nOtherwise type 'exit' to exit the program.")
    else:
        print(f"There are no known student records associated with the UID '{searchedID}'\nMake sure to only use non-decimal numbers and no letters such as 'u'.\nIf you made a mistake please re-enter the UID. Otherwise type 'exit' to quit the program.")
            
''' 

#for quick testing with the following UID lookup program, copy and paste the following without the triple quotes into the console or terminal while the script is running.
'''
123
James
Farnsworth
Infosys
234
Jimmy
Smithy
Cyber
345
Josh
Brown
Arts
'''
#the following block of code first introduces the user to the lookup tool and then creates a loop with an exit varible. It asks the user for a UID or to type 'exit' to end the program.     
print("\nWelcome to the UID lookup!\nPlease insert a valid UID to search for.\nOtherwise to quit the program please type 'exit'.")
exit = 0
while exit == 0:
    searchedID = input("\nEnter a valid student UID to search for: ")
    
    if searchedID.lower() in {"exit", "quit"}:
        exit = 1
        continue
    
#if the user enters a valid UID then get the records associated with the UID and print them out. It then asks if the user would like to enter into the major edit tool.
    elif searchedID in studentRecords.get(searchedID):
        student = studentRecords.get(searchedID)        
        #print(f"Here is the record associated with the student UID '{searchedID}':\nUID:{student[0]}\nfirstname:{student[1]}\nsecondName:{student[2]}\nmajor:{student[3]}\n")
        print("I have found the student %s %s with the %s UID in the major of %s.\n"%(student[1].capitalize(), student[2].capitalize(), student[0], student[3].capitalize()))
        print("Would you like to change a student's major? If so type 'major' or 'edit'.\nOtherwise type anything else to exit this menu.\n")
        majorEdit = input("Type 'major' to enter major edit mode: ")
        
#major edit mode is similar to the UID lookup except when it searches for the student associated with the UID it asks the user to give it a different major name to change the current major from.        
        if majorEdit.lower() in {"major", "edit"}:
            print("You have entered major edit mode.")
            majorUIDChange = input("\nPlease enter the student UID you wish to edit the major of:")
            majorNameChange = input("\nPlease enter the new major name: ")
            
#if the uid exists get the record associated with uid then change the uid major to the new user inserted one. Also print out the results of the change.         
            if majorUIDChange in studentRecords.get(searchedID):
                student = studentRecords.get(majorUIDChange)
                oldMajorName = student[3]
                student[3] = majorNameChange
                
                print(f"You have changed student {majorUIDChange}'s major to {student[3].capitalize()}!\nreturning to UID lookup.")
#all below bits of code are fail cases or exit causes.            
            else:
                print(f"There are no known student UID by the number '{majorUIDChange}'.\nMake sure to only use non-decimal numbers and no letters such as 'u'.\nIf you made a mistake please re-enter the UID. Otherwise type 'exit' to quit the program.")
          
        elif majorEdit.lower() in {"exit", "quit"}:
            exit = 1
            continue
            
        else:
            continue
            
    else:
        print(f"There are no known student records associated with the UID '{searchedID}'.\nMake sure to only use non-decimal numbers and no letters such as 'u'.\nIf you made a mistake please re-enter the UID. Otherwise type 'exit' to quit the program.")
           
    
    