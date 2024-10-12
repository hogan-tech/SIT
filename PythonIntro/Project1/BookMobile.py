from BookMobileFunctions import *


def main():
    booksDict: Dict[str, List[str]] = {}
    categoriesSet: Set[str] = set()
    booksLoaded = False
    welcome()

    while True:
        choice = menu()
        if choice == 1:
            booksDict, categoriesSet = loadBooks()
            print("Books loaded successfully!")
            print(booksDict, categoriesSet)
            booksLoaded = True

        elif choice == 2:
            if not booksLoaded:
                print("You need to load the book file first!")
            else:
                try:
                    reviewsList = loadReviews(booksDict)
                    print(reviewsList)
                    print("Reviews loaded successfully!")
                # I use LookupError to get error message
                except LookupError as e:
                    print(e)
                
        elif choice == 7:
            goodBye()
            break
        else:
            print("Invalid option. Please input from 1 ~ 7.")


if __name__ == "__main__":
    main()



"""
Input
1
books10.csv
books10rating.csv
"""