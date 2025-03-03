#imports the statisics library into the document
import statistics

#exercise 1, creates varibles then prints them all in serperate lines with var#= placed beforehand.
print("Exercise 1")

var1, var2, var3 = 10, 15, 20
print(f"var1={var1}\nvar2={var2}\nvar3={var3}\n")

#exercise 2, creates a number's list and then averages 
print("Exercise 2")
# numList = [3,7,8,2,10]
# avg = sum(numList) / len(numList)
# print(f"{avg}\n")

#without using a list
average = (3 + 7 + 8 + 2 + 10) / 5
print(average)

#exercise 3, going through and adding, subtracting and multiplying x using the respective opperators
print("\nExercise 3")

#varible definitions
# x, y = 3, 0
# addList = [34,22,65,78,99]
# subList = [44,33,22,11]
# multiList = [5,4,3,2,1]
# allList = [addList,subList,multiList]

# #adding, subtracting, and multiplying x through each respective list
# for y in addList:
    # x += y
# print(x)

# for y in subList:
    # x -= y
# print(x)

# for y in multiList:
    # x *= y
# print(f"{x}\n")

#without using fancy loops or lists (pain, please no one ever do it this way for everyone's sake!)
x = 3
x += 34 
x += 22 
x += 65 
x += 78 
x += 99
print(x)
x -= 44
x -= 33
x -= 22
x -= 11
print(x)
x *= 5
x *= 4
x *= 3
x *= 2
x *= 1
print(x)

#exercise 4, simple printed remainder math
print("\nExercise 4")

print(100%23)

#exercise 5, creates basic varibles for an account which are then added to a list which is then added to a dictionary which can be updated dynamically if need be. (First part is static, defined function part is dynamic which is functioned and it's call is commented out for the purposes of the homework)
#staticly defined varibles for basic testing and assignment, I put a version with input variables instead to showcase a typical simply verison of an account creator after this static version.
print("\nExercise 5")
name = "Alice Vahn"
investment = 10000
interestRate = 0.0532
account = [name, investment, interestRate]
accountDic = {}

id = len(accountDic) + 1
accountDic[id] = account

print(f"{accountDic.get(id)[0]} has invested ${accountDic.get(id)[1]:,} into a savings account that has a {100*accountDic.get(id)[2]:.2f}% interest rate\n")

#dynamic account adder, uncomment function call to test yourself! :)
#note: the data is stored on memory not rom so don't be surprised if you make 100 accounts and you exit the script and the accounts cease to exist. I didn't make error checks, so make sure you put in a string, int, and then float in that order or it will error out.
def bankAccountCreator():
    accountDic = {}
    exit = 0
    while exit == 0:
        
        name = input("\nPlease insert first and last name of account user: ")
        investment = int(input("Please insert account investment of user: "))
        interestRate = float(input("Please insert the raw investment rate in decimal form (e.g. \"5.32%\" --> \"0.0532\"): "))
        account = [name, investment, interestRate]
        

        id = len(accountDic) + 1
        accountDic[id] = account

        print(f"{accountDic.get(id)[0]} has invested ${accountDic.get(id)[1]:,} into a savings account that has a {100*accountDic.get(id)[2]:.2f}% interest rate")
        print(f"\nCurrent account database:\n{accountDic}")
        
        userexit = input("\nDo you want to add more accounts? If so press enter to continue.\nOtherwise type \"quit\" to exit the Bank Account Creator: ")
        if userexit in {"exit", "quit"}:
            exit = 1
            print("Affirmative! Moving to Exercise 6. Goodbye! :)\n")
            
    return accountDic

#I'm so sad I can't forward delcare in Python, can't even do while() loop either! What's even the point!? :(
#uncomment below to try dynamic account creator!
#bankAccountCreator()

#Exercise 6 create a string and int, then combine the value of the string with the integer. Aka convert a string varible to an int to then add them together
print("Exercise 6")
retirementAge = "67"
x = 3
print(int(retirementAge) + 3)

#Exercise 7 I already essentially did this in exercise 2, but basically get a list and average the numbers in said list. To spice things up I'm using the mean function from the statistics module/library to average the the grades. And to prove it works correctly I will do the manual method as well. 
print("\nExercise 7")
grades = [90,89,93,75]
print(f"mean function method answer: {statistics.mean(grades)}")

print(f"manual method answer: {sum(grades) / len(grades)}")

#Exercise 8 creates a dictionary which we then assign a bunch of key value pairs and then print all the values using the dictionary keys for each value.
print("\nExercise 8")
starwars = {}
starwars = {"U123456":"Han Solo", "U987654":"Luke Skywalker", "U876543":"Darth Vader", "U32145":"Ben Kenobi"}
print(starwars["U123456"], starwars["U987654"], starwars["U876543"], starwars["U32145"])

