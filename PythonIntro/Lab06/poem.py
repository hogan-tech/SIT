# Author: Hogan Lin
# Date: Oct 11th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program reads the title, author, and lines of a poem from a file specified
#              by the user. It then generates a summary of the poem, including the title, author,
#              number of lines, and a preview of the first three lines, and writes this summary to
#              'Output.txt'. If the input file doesn't exist, the program reprompts the user.


import os


def main():
    """
    This main function summarizes a poem by reading its title, author, and lines from an input file and writing
    a summary to an output file.
    """
    poemTitle = ""
    poemAuthor = ""
    poemLines = []
    fileName = ""

    while True:
        fileName = input(
            "Please input the name of the poem you wish summarized: ")
        if os.path.exists(fileName):
            break
        else:
            print(
                f"{fileName} does not exist! Please input the name of the poem you wish summarized.")

    with open(fileName, 'r') as file:
        poemTitle = file.readline().strip()
        poemAuthor = file.readline().strip()

        for line in file:
            poemLines.append(line.strip())

    with open('Output.txt', 'w') as outputFile:
        outputFile.write(f"The name of the poem is {poemTitle}\n")
        outputFile.write(f"The author of the poem is {poemAuthor}\n")
        outputFile.write(
            f"The number of lines in the poem is {len(poemLines)}\n")
        outputFile.write("A preview of the poem is:\n")

        for i in range(min(3, len(poemLines))):
            outputFile.write(poemLines[i] + '\n')

    print(f"The summary has been written to Output.txt")


if __name__ == "__main__":
    main()
