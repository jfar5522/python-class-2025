def inputFromKeyboard(msg):
    return input(msg)

def openFile(filename):
    return open(filename)

def printFile(filepath):
    with open(filepath) as file:
        for line in file:
            print(line)