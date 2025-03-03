#creates string varible, then creates varible that takes the numbers from string varible and turns them into a float varible which it then adds 2.23 to as well. Finally prints addedMoney var.
wallet = "I have $15.12 in my wallet."
addedMoney = wallet[8:14]
addedMoney = float(addedMoney)
addedMoney = addedMoney+2.23
print("$%.2f"%(addedMoney))

#creates array var, it then prints the 8-12 places of the array, aka September-December
months = ["January", "February", "March", "April", "May", "June", "July", "Augest", "September", "October", "November", "December"]
print(months[8:12])

#creates an array var then painstakingly appends each months array values one at a time instead of using a for loop... spaghetti code at it's finest! Also prints the array as well I guess.
newList = []
newList.append(months[0])
newList.append(months[1])
newList.append(months[2])
newList.append(months[3])
newList.append(months[4])
newList.append(months[5])
newList.append(months[6])
newList.append(months[7])
newList.append(months[8])
newList.append(months[9])
newList.append(months[10])
newList.append(months[11])
print(newList)

#creats array, then inserts 7 at the second position of the array. Prints array.
numList = [5,6,8,9]
numList.insert(2, 7)
print(numList)