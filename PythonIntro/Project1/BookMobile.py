from BookMobileFunctions import *


def main():
    booksDict: Dict[str, List[str]] = {}
    categoriesSet: Set[str] = set()

    welcome()

    while True:
        choice = menu()
        if choice == 1:
            booksDict, categoriesSet = loadBooks()
            print("Books loaded successfully!")
            print(booksDict, categoriesSet)
        elif choice == 7:
            goodBye()
            break
        else:
            print("Invalid option. Please input from 1 ~ 7.")


if __name__ == "__main__":
    main()
