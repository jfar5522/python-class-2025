#simple function used to multiply two parameter variables
def multiply(a, b):
    a = a * b
    return a
    
print(multiply(432, 1780))

print("")

#creates a number appending function which optionally broadcasts the number added and the list appended to.
list = []

def numAppend(num, list, broadcast=0):
    list.append(num)
    if broadcast == 1:
        print(f"Appended {num} to your list which now contains the following:\n{list}")
    
numAppend(5, list)
numAppend(2, list)
numAppend(7, list)
numAppend(8, list, 1)

print("")

#creates two functions first of which creates lists with a parameter length, second function takes a list and returns the odd values of said list. Finally we combine the two in a single print statement.
def listCreator(length=10):
    list = []
    
    for counter in range(length):
        list.append(counter + 1)
        
    return list
    

def oddList(list):
    nList = []
    
    for v in list:
        if (v % 2 != 0):
            nList.append(v)
            
    return nList

#print(listCreator(100))
  
print(oddList(listCreator(100)))

print("")

#first function takes user input and returns it based on a parameter. Second takes a string and removes the vowels from it. We then combine the functions and print them.
def uInput(ui):
    return input(ui)
    
def vowelReturn(string):
    vowelessString = ""
    index = 0
    
    for char in string: #every string is a list of characters, so it's only fitting we'd name the loop varible "char". E.g. "for every character in the string".
        if char in ("a", "e", "i", "o", "u", "y"):
            continue
        else:
            vowelessString += char
            
    return vowelessString

            
print(vowelReturn(uInput("Type a sentence and watch as the vowels are removed: ")))
