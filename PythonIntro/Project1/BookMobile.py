# Author: Hogan Lin
# Date: Oct 12th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description:  A menu-driven Python program for managing and analyzing book data and reviews. 
#               Users can load book/review data from CSV files, list books by category, view book details, 
#               calculate author ratings, and find the most helpful reviewer. 
#               The program ensures data is loaded before certain actions can be performed, and uses pandas for efficient data handling.

from BookMobileFunctions import *


def main():
    booksDict: Dict[str, Dict] = {}
    categoriesSet: Set[str] = set()
    booksLoaded = False
    reviewsLoaded = False
    welcome()

    while True:
        choice = menu()
        if choice == 1:
            booksDict, categoriesSet = loadBooks()
            print("Books loaded successfully!")
            booksLoaded = True

        elif choice == 2:
            if not booksLoaded:
                print("You need to load the book file first!")
            else:
                try:
                    reviewsList = loadReviews(booksDict)
                    print("Reviews loaded successfully!")
                    reviewsLoaded = True
                # I use LookupError to get error message
                except LookupError as e:
                    print(e)
        elif choice == 3:
            if not booksLoaded:
                print("You need to load the book file first!")
            else:
                listBooksByCategory(booksDict, categoriesSet)
        elif choice == 4:
            if not reviewsLoaded and not booksLoaded:
                print("You need to load the reviews file and book file first!")
            else:
                showBookDetails(booksDict, reviewsList)
        elif choice == 5:
            if not reviewsLoaded:
                print("You need to load the reviews file first!")
            else:
                showAuthorRatings(booksDict, reviewsList)
        elif choice == 6:
            if not reviewsLoaded:
                print("You need to load the reviews file first!")
            else:
                showHelpfulReviewer(reviewsList)
        elif choice == 7:
            goodBye()
            break
        else:
            print(f"{choice} is not a valid option! Try again.")


if __name__ == "__main__":
    main()
