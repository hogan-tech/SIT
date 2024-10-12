# Author: Hogan Lin
# Date: Oct 11th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program prompts the user for the name of a file containing numbers separated by commas,
#              converts the numbers into ASCII art using helper functions from pbnFunctions.py, and writes the result
#              to a file called 'painting.txt'. The program also informs the user of the location of the output file.



import pbnFunctions


def main():
    """
    main()
    The main function that serves as the entry point of the program. It retrieves the file name from the user,
    processes the file to generate ASCII art, and informs the user of the location of the output.

    :return: None
    """
    fileName = pbnFunctions.getFileName()
    pbnFunctions.processFile(fileName)
    print("Your image can be found in painting.txt. Enjoy!")


if __name__ == "__main__":
    main()
