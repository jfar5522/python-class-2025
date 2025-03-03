#input name, capitalize name, search for name in name list.
name = input("Please enter your first name: ")
name = name.capitalize()
nameList = { "Bob", "Lisa", "Andrew", "Jennifer" }

if name in nameList:
    print("Name Found")
else:
    print("Name NOT found")
    

#input number between 1 and 30, program looks and sees where the number lays and says whether the number is between 1 and 10, 10 and 20, or 20 and 30.
userNumber = int(input("\nPlease enter a number between 1 and 30: "))
counter = 0

#I'm sorry idk why I always get side tracked, basically counts how many times you input the wrong number and the computer becomes passive agressive. I just wanted to put a little fun in the program.
while (userNumber < 1  or userNumber > 30) and counter < 10:
    userNumber = int(input("Please make sure to enter a number between 1 and 30: "))
    counter += 1

while (userNumber < 1 or userNumber > 30) and counter >= 10 and counter < 20:
    userNumber = int(input("I said enter a number between 1 and 30: "))
    counter += 1

if (userNumber < 1 or userNumber > 30) and counter >= 20:
    print("\nYou're just doing this intentionally now...\n")

while (userNumber < 1 or userNumber > 30) and counter >= 20 and counter < 50:
    userNumber = int(input("Enter a number between 1 and 30 or we will be here forever: "))
    counter += 1

if (userNumber < 1 or userNumber > 30) and counter >= 50:
    print("\nI'm not going to encourage this behavior anymore.\n")
    
while (userNumber < 1 or userNumber > 30) and counter >= 50:    
    userNumber = int(input("Enter a number between 1 and 30... or don't I've stopped caring after the 50th try: "))
    counter += 1
    
if counter >= 50:
    print(f"\nYou've entered a wrong number { counter } times... Congrats\nHope you're proud of yourself.\n")
    print("\"insert_achievement_about_being_wrong_here\"\n")
    
#check where the number is in relation to 1, 10, 20, and 30.    
if userNumber >= 1 and userNumber < 10:
    print("Your number is between 1 and 10\n")
elif userNumber >= 10 and userNumber < 20:
    print("Your number is between 10 and 20\n")
else:
    print("Your number is between 20 and 30\n")
   
   
#create dictionary and use a for loop to search and print dictionary values and keys.   
studentMajorDic = {"Mark":"IS", "Laura":"CIS", "Adam":"Finance", "Lisa":"Undeclared"}

for student in studentMajorDic:
    print(f"The student {student} is in the {studentMajorDic.get(student)} major")
    
print("")

#2D array of values from 0 to 9, change size of terminal to move how the array looks
twoDArray = []
for x in range(10):
    for y in range(10):
        twoDArray.append("[%d, %d]"%(x,y))
        
#using array to print out 2d array instead of printing it out as we build it.
for point in twoDArray:
    print(point, end = " ")
    if point[4] == "9":        
        print("")

print("")


#normal version 
print("")   
for x in range(10):
    for y in range(10):
        print("[%d, %d]"%(x,y), end=" ")
    print("")

