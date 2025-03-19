#note all files created are assumed to be data files and therefore will be created
#in the "data" directory

#reads and prints every line of the file specified in parameter. Also returns a
#list of all the lines.
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
                     file=open(filePath,"w")
                     file.close()
                     return filePath
                except FileNotFoundError: # if "data" folder doesn't exist... too
#lazy to have it create it for you
                     file=open(fileName, "w")
                     file.close()
                     return fileName
            else: # if reading and not writing file
                print(f"File {fileName} does not exist in either the current or data directory for reading! Returning null!")
                return None


#read entire file, optionally able to print file with print paramter
def fileReader(fileName, newlines=False, printbool=False):
    filePath = fileFinder(fileName)
    if filePath is None:
        return None

    lineList = []

    #put "with" here as an example of a way to open a file without having to manually close it each time
    if(newlines):
        with open(filePath) as file:
            for line in file:
                lineList.append(line)
                if(printbool):
                    print(line)
            return(lineList)
    else:
        with open(filePath) as file:
            for line in file:
                #remove new line string
                line = line.rstrip("\n")

                #test if integer or not
                try:
                     line = int(line)
                except ValueError:
                     line = str(line)

                lineList.append(line)
                if(printbool):
                    print(line)
            return(lineList)

#reads the line specified of the named file
def fileLineReader(fileName, line):
            filePath = fileFinder(fileName)
            if filePath is None:
                return None

            with open(filePath) as file:
                for lineI in range(line-1):
                    file.readline()
                sLine = file.readline()
                return sLine


#writes a new/to a file, can change mode to write but defaults to append
def fileAppender(fileName, content):
        mode = "a"
        filePath = fileFinder(fileName, mode)

        with open(filePath, mode) as file:
            file.write(content)


#writes on or over a specified line of the named file
def fileWriter(fileName, content, line=0, clearFile=False, mode="w"):
    """
    Write integers or a list of integers to a specific line in a file.

    Args:
        fileName (str): Name of the file to write to.
        content (int or list): A single integer or list of integers to write.
        line (int): The line number to write to (1-based index). Ignored if content
is a list.
        clearFile (bool): If True, clear the file before writing.
        mode (str): File mode ("w" for write, "a" for append).
    """
    filePath = fileFinder(fileName, "w")

    lines = fileReader(fileName)

    # if lines is null error out. This should NEVER happen
    if lines is None:
        raise ValueError(f"Failed to read {filePath}")
    # make sure line is a positive integer and nothing else
    if not isinstance(line, int) or line < 0:
        raise ValueError("Line number must be a positive integer")

    # Ensure content ends with a newline for consistency (if not used you will be deleting a line)
    if isinstance(content, (str, int)):
        content = str(content)
        if not content.endswith("\n"):
            content += "\n"

        # If clearFile is True or anything close to true, ignore existing lines and pad with newlines
        if clearFile or clearFile == 1 or clearFile in {"1", "one", "yes", "Yes",
"true", "True" "on", "active"}:
            lines = [] # Clear existing content in memory
            while len(lines) < line: # add new lines (enter characters) to list until you reach the target line of list
                lines.append("\n")
            lines[line - 1] = content
        else:
            # Pad with empty lines if the target line exceeds current file length
            while len(lines) < line:
                lines.append("\n")
            # Replace the specified line with the new content
            lines[line - 1] = content

        with open(filePath, mode) as file:
            file.writelines(lines)

    #if using a list rather than a single string, very effective when using one of the fileReaders
    elif isinstance(content, list):
        with open(filePath, mode) as file:
            for line in content:
                line = str(line)
                if not line.endswith("\n"):
                    line += "\n"
                file.write(line)