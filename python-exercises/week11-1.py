try:
    import filelib
except ModuleNotFoundError:
    import sys
    import os

    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib")))
    import filelib

#filelib.fileReader("first-file.txt")
#filelib.fileLineReader("sentences.txt",1)
#filelib.fileWriter("sentences.txt","hi there!")

# Welcome! All the code is in my modual file this file is to call functions or write code with my lib functions!
# Please look over my filelib.py modual file for code specifics.
# filelib.py should be included either in the lib folder, if you're looking at my github, or included in the submission files!

#creates resorting txt file and adds a list of strings on each line
filelib.fileWriter("resorting.txt",["one","two","three","four"])

#will maybe use a range parameter function in the future but for now takes the
#specific lines and adds them to sorted
filelib.fileWriter("sorted.txt",
[filelib.fileLineReader("resorting.txt",3),filelib.fileLineReader("resorting.txt",4)])
#will maybe use a range parameter function in the future but for now takes the specific lines and adds them to sorted
filelib.fileWriter("sorted.txt", [filelib.fileLineReader("resorting.txt",3),filelib.fileLineReader("resorting.txt",4)])


#writes 20 lines to the resorting file
filelib.fileWriter("resorting.txt",["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"
                                        ,"thirteen", "fourteen","fifteen","sixteen","seventeen","eightteen","nineteen","twenty"])

#adds the last 10 lines to the sorted file. Functions are broken up to avoid running them multiple times.
resorting = filelib.fileReader("resorting.txt")
sortedF = []
for line in range(9,20):
    sortedF.append(resorting[line])

filelib.fileWriter("sorted.txt",sortedF)

#Go backwards really fast! Rewrites the sorted file to be backwards.
rsorted = []
r = len(sortedF) - 1
for line in sortedF:
    rsorted.append(sortedF[r])
    r -= 1

filelib.fileWriter("sorted.txt",rsorted)

#create new files "keys.txt" and "values.txt" respectively, then combines the keys and values into a sorted dictionary, finally prints.

filelib.fileWriter("keys.txt", [8977,3248,9837,2123])
filelib.fileWriter("values.txt", ["Katy Perry", "Marshal Mathers", "Jason Mamoa", "Julia Roberts"])

keys = filelib.fileReader("keys.txt")
values = filelib.fileReader("values.txt")

#gives dic keys and then assigns the keys to values
dic = {}
for key, value in zip(keys, values):
    dic[key] = value

sortedDic = sorted(dic.items())

print(sortedDic)




