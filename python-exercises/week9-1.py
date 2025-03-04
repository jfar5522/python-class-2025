#for this program to work based on the file structure I'm using, check out my github repo!: https://github.com/jfar5522/python
#if you're interested in viewing my previous work check out my old github page!: https://github.com/James1323


# Get the parent directory and add "lib" folder to sys.path.
try:
    import myreadfile

except ModuleNotFoundError:
    import sys
    import os

    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib")))
    import myreadfile

#open and print entire file
try:
    file=open("first-file.txt")
    for line in file:
        print(line)
    file.close()

except FileNotFoundError:
    import os
    print("Current Working Directory:", os.getcwd())

    scriptDir = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(scriptDir, "..", "data", "first-file.txt")

    #put "with" here as an example of a way to open a file without having to manually close it each time
    with open(filePath) as file:
        for line in file:
            print(line)

print("")

#have user decide what line to print from the file
try:
    file=open("first-file.txt")
    fileRead = input("Type between 1 and 3 in which each number is the printout of lines of the 'first-file.txt' file: ")
    if fileRead in "1":
        print(file.readline())
    elif fileRead in "2":
        print(file.readline())
        print(file.readline())
    elif fileRead in "3":
        print(file.readline())
        print(file.readline())
        print(file.readline())
    file.close()

except FileNotFoundError:
    fileRead = input("Type between 1 and 3 in which each number is the printout of lines of the 'first-file.txt' file: ")
    file=open(filePath)
    if fileRead in "1":
        print(file.readline())
    elif fileRead in "2":
        print(file.readline())
        print(file.readline())
    elif fileRead in "3":
        print(file.readline())
        print(file.readline())
        print(file.readline())
    file.close()




#better way of going through a file
try:
    file=open("first-file.txt")
    fileRead = input("Enter 1 and 3 again and it will print the specific line of the file this time: ")

    i = 0
    while True:
        i += 1
        line=file.readline()
        if not line:
            break;
        if i == 1 and fileRead == "1":
            print(line)
        if i == 2 and fileRead == "2":
            print(line)
        if i == 3 and fileRead == "3":
            print(line)
        
    file.close()

except FileNotFoundError:
    file=open(filePath)
    fileRead = input("Enter 1 and 3 again and it will print the specific line of the file this time: ")

    i = 0
    while True:
        i += 1
        line=file.readline()
        if not line:
            break;
        if i == 1 and fileRead == "1":
            print(line)
        if i == 2 and fileRead == "2":
            print(line)
        if i == 3 and fileRead == "3":
            print(line)
        
    file.close()

#user file selector and printer
try:
    filename=myreadfile.inputFromKeyboard("Enter a local filename or an absolute file path and watch as it prints it all out!\n: ")
    file=myreadfile.openFile(filename)
    myreadfile.printFile(filename)
    file.close()

except FileNotFoundError:
    print("File not found!\nMake sure you have entered the file name or path correctly.")


