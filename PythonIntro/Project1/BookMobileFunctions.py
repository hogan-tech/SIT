# Author: Hogan Lin
# Date: Oct 12th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: 

import os
from typing import Dict, List, Set, Tuple


# Because the data type is a little bit complicate, I add type to avoid the error
def loadBooks() -> Tuple[Dict[str, List[str]], Set[str]]:
    """
    Load a file containing a list of books.

    Returns:
    - Dictionary of Lists containing each of the books from the file
    - Set containing all of the literary categories of the books
    """
    booksDict: Dict[str, List[str]] = {}
    categoriesSet: Set[str] = set()

    while True:
        fileName = input(
            "Please enter the name of the book data csv file: ")
        if os.path.exists(fileName):
            break
        else:
            print("File does not exist.")

    with open(fileName, "r") as file:
        for line in file:
            line = line.strip()
            title, author, category, description, publisher, year = line.split(
                ",")
            booksDict[title] = [author, category, description, publisher, year]
            categoriesSet.add(category.lower())

    return booksDict, categoriesSet



def welcome() -> None:
    print("Welcome to the project 1 : Book Mobile")


def goodBye() -> None:
    print("Thank you, goodbye!")


def menu() -> int:
    """
    Show a menu and get the user's choice.

    Returns:
    - int: The number of the option the user chose
    """
    print("\nMenu:")
    print("1. Loading the book file")
    print("2. Loading the book review file")
    print("3. Outputting books by literary category")
    print("4. Outputting a book’s details")
    print("5. Outputting the average author ratings")
    print("6. Outputting the most helpful reviewer")
    print("7. Quitting")
    choice = input("Please choose an option (1-7): ")

    return int(choice)
