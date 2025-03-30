#note all files created are assumed to be data files and therefore will be created in the "data" directory

#finds or creates file specified
def fileFinder(fileName, mode="r"):
    # Check current directory for file
    try:
        file=open(fileName)
        file.close()
        return fileName
    
    # check data folder for file
    except FileNotFoundError:
        import os
        #print("Current Working Directory:", os.getcwd())

        scriptDir = os.path.dirname(os.path.abspath(__file__))
        filePath = os.path.join(scriptDir, "..", "data", fileName)
        try:
            file=open(filePath)
            file.close()
            return filePath
        
        except FileNotFoundError:
            # check if mode is "w" or "a" else return null
            if mode in {"w", "a"}:
                try:
                    file=open(filePath,"w") # create in data folder
                    file.close()
                    return filePath
                except FileNotFoundError: # if "data" folder doesn't exist... too lazy to have it create it for you so it creates file to the program's current directory
                    file=open(fileName, "w")
                    file.close()
                    return fileName
            else: # if reading and not writing file
                print(f"File {fileName} does not exist in either the current or data directory for reading purposes!\nReturning null!")
                return None

    
#read entire file, optionally add new return lines after each line, also able to print file with print paramter
def fileReader(fileName, fileOrList=False, newlines=False, printbool=False):
    """
    read entire file, optionally add new return lines after each line, also able to print file with print paramter
    
    Args:
        fileName (str): Name of the file to read to.
        fileList (bool): False means lines list for writing into a file. True means normal list to grab items from.
        newlines (bool): New blank line after each line.
        printbool (bool): Print file to terminal.
    """

    filePath = fileFinder(fileName)
    if filePath is None:
        return None
    
    lineList = []

    #add new lines, \n, after each line
    if newlines:
        with open(filePath) as file:
            for line in file:
                lineList.append(line)
                if printbool:
                    print(line)
            return(lineList)
    else:
        with open(filePath) as file:
            for line in file:

                #remove new line string
                if(fileOrList):
                    line = line.rstrip("\n")

                #test if integer or not
                try:
                    line = int(line)
                except ValueError:
                    line = str(line)

                lineList.append(line)
                if printbool:
                    print(line)
            return(lineList)

#TODO: turn function into "fileRangeReader" to read a specific range of lines while returning that range as a list.
#reads the line specified of the named file 
def fileLineReader(fileName, line):            
            filePath = fileFinder(fileName)
            if filePath is None:
                return None

            with open(filePath) as file:
                for i in range(line-1):
                    file.readline()
                sLine = file.readline()
                return sLine

#NOTE obsolete, don't bother using unless you feel like it and want it write weirdly into a file.            
#writes a new/to a file, can change mode to write but defaults to append
def fileAppender(fileName, content):
        mode = "a"
        filePath = fileFinder(fileName, mode)

        with open(filePath, mode) as file:
            file.write(content)


#writes on or over a specified line of the named file
def fileWriter(fileName, content, line=1, clearFile=False, mode="w"):
    """
    Write strings or integers over lines in a file, can use lists to achieve the same thing.
    
    Args:
        fileName (str): Name of the file to write to.
        content (string, int or list): A single integer/string or list of integers/strings to write.
        line (int): The line number to write at or start writing at (1-based index).
        clearFile (bool): If True, clear the file before writing.
        mode (str): File mode, archaic don't use unless you really want to. ("w" for write, "a" for append)
    """

    filePath = fileFinder(fileName, "w")

    fileContent = fileReader(fileName)

    # if fileContent is null error out. This should NEVER happen as the write mode should create the file!
    if fileContent is None:
        raise ValueError(f"Failed to read {filePath}")
    
    # make sure line is a positive integer and nothing else.
    if not isinstance(line, int) or line < 0:
        raise ValueError("Line number must be a positive integer.")
    
    # if it's not a string or list, turn it into a string.
    if not isinstance(content, (str, list)):
        content = str(content)

    # If clearFile is True or anything close to true, ignore existing lines and pad with newlines.
    if clearFile or clearFile == 1 or clearFile in {"1", "one", "yes", "Yes", "true", "True" "on", "active"}:
        fileContent = []  # Clear existing content in memory.




    if isinstance(content, str):
        # Pad with empty lines if the target line exceeds current file length.
        while len(fileContent) <= line:
            fileContent.append("\n")
        # if not content.endswith("\n"):
        #     content += "\n"
            
        # Replace the specified line with the new content.
        fileContent[line - 1] = content

        #input modified fileContent back into file.
        with open(filePath, mode) as file:
            file.writelines(fileContent)

    #if using a list rather than a single string, very effective when using filereader as it outputs a list.
    elif isinstance(content, list):

        with open(filePath, mode) as file:
            # first add spaces to meet what line the user wants to type from, 
            # then create space for the new content the user wants to write
            while len(fileContent) <= line + len(content) - 2:
                fileContent.append("\n")
            try:
                for iLine in content:
                    iLine = str(iLine)
    
                    
                    if not iLine.endswith("\n"):
                        iLine += "\n"


                    fileContent[line - 1] = iLine
                    line += 1

                file.writelines(fileContent)
            except TypeError:
                print("There was a type error in your list! Make sure you're inputting content that can be turned into a string."
                "\nLists inside lists are not allowed... yet.")
    else:
        raise TypeError("Whatever content you have inputed ")

