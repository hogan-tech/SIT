# Author: Hogan Lin
# Date: Oct 11th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program reads a file containing numbers separated by commas,
#              converts those numbers into specific symbols (representing ASCII art),
#              and writes the resulting art to a file named 'painting.txt'. The user is repeatedly
#              prompted for a valid file name if the specified file does not exist.

import os


def getFileName():
    """
    getFileName()
    Prompts the user for a valid file name and checks for its existence.

    :return: The valid file name input by the user.
    :rtype: str
    :raises FileNotFoundError: Repeatedly prompts the user until a valid file name is given.
    """
    while True:
        fileName = input("Please input the file you wish to have painted: ")
        if os.path.exists(fileName):
            return fileName
        else:
            print(f"{fileName} does not exist! Please input a valid file name.")



def convertLine(line):
    """
    convertLine(line)
    Converts a line of comma-separated numbers into specific ASCII symbols.

    :param line: A string containing numbers separated by commas.
    :type line: str
    :return: A string where the numbers have been converted to corresponding symbols.
    :rtype: str
    """
    line = line.strip()
    newLine = ""

    numbers = line.split(',')

    for num in numbers:
        if num == '1':
            newLine += " "
        elif num == '2':
            newLine += ","
        elif num == '3':
            newLine += "_"
        elif num == '4':
            newLine += "("
        elif num == '5':
            newLine += "O"
        elif num == '6':
            newLine += ")"
        elif num == '7':
            newLine += "-"
        elif num == '8':
            newLine += '"'

    return newLine


def processFile(filename):
    """
    processFile(filename)
    Reads an input file line by line, converts the contents from numbers to ASCII symbols, 
    and writes the resulting output to 'painting.txt'.

    :param filename: The name of the input file containing the numbers to be converted.
    :type filename: str
    :return: None
    :raises Exception: If there's an error processing the input or output files.
    """
    try:
        with open(filename, 'r') as inputFile, open('painting.txt', 'w') as outputFile:
            for line in inputFile:
                newLine = convertLine(line)
                outputFile.write(newLine + '\n')
    except Exception as e:
        print(f"Error processing file: {e}")
