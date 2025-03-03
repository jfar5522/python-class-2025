#creates list then appends 5 to the list
list = [1,2,3,4]
list.append(5)
#print(list)

#deletes 5 in the list which is in the 4th position of said list
del list[4]
#print(list)

#inserts 2.5 at the 2nd position
list.insert(2, 2.5)
#print(list)

#makes a new list then extends first list to add the new list
nList = [8,7,6,1.5]
list.extend(nList)
#print(list)

#sort list by values from least to greatest.
list.sort()
# print(list)
