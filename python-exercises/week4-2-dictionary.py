#create dictionary and get "Mark" from that dictionary.
dict = {1:"Tom", 2:"Carl", 3:"Mark", 4:"Tim"}
print(dict.get(3))

#print out the length, keys, and values of the dictionary.
print(len(dict))
print(dict.keys())
print(dict.values())

#add the key pair 0 and none to the dictionary and print the dictionary
dict.update({0:"none"})
print(dict)

#sort the dictionary by key numbers from least to greatest
dict = sorted(dict.items())
print(dict)