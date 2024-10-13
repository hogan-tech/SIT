# Author: Hogan Lin
# Date: Oct 12th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description:

from collections import defaultdict
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
    booksDict: Dict[str, Dict] = {}
    categoriesSet: Set[str] = set()

    while True:
        fileName = input(
            "Please enter the name of the book data csv file: ")
        if os.path.exists(fileName):
            break
        else:
            print("File does not exist.")

    with open(fileName, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            line = line.strip()
            title, description, author, publisher, publishedDate, category = line.split(
                ",")
            bookDetail = {
                "title": title,
                "description": description,
                "author": author,
                "publisher": publisher,
                "publishedDate": publishedDate,
                "category": category
            }
            booksDict[title] = bookDetail
            categoriesSet.add(category)

    return booksDict, categoriesSet


def loadReviews(booksDict: Dict[str, List[str]]) -> List[List]:
    """
    Load a file containing a list of book reviews.

    Parameters:
    - booksDict: Dictionary of book information

    Returns:
    - List containing each of the book reviews from the file
    """
    reviewsList: List[List] = []

    while True:
        fileName = input(
            "Please enter the name of the book review data csv file: ")
        if os.path.exists(fileName):
            break
        else:
            print("File does not exist.")

    with open(fileName, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            line = line.strip()
            id, title, price, userId, profileName, helpfulness, score = line.split(
                ",")
            if title not in booksDict:
                raise LookupError(
                    f"Book '{title}' not found in the book dictionary.")
            reviewsList.append(
                [id, title, price, userId, profileName, helpfulness, score])

    return reviewsList


def listBooksByCategory(booksDict: Dict[str, List[str]], categoriesSet: Set[str]) -> None:
    """
    List all books within a literary category.

    Parameters:
    - booksDict: Dictionary of book information
    - categoriesSet: Set of literary categories
    """
    print("\nAvailable categories:")
    for i, category in enumerate(categoriesSet, start=1):
        print(f"{i}. {category}")

    while True:
        category = input("Please enter a category: ").strip()
        if category in categoriesSet:
            break
        else:
            print("Invalid category.")

    print(f"Books in the '{category}' category:")

    for i, (booksKey, booksValue) in enumerate(booksDict.items(), start=1):
        if booksValue['category'] == category:
            print(
                f"\nTitle: {booksValue['title']} \nAuthor: {booksValue['author']}")


def showBookDetails(booksDict: Dict[str, List[str]], reviewsList: List[List]) -> None:
    """
    Show detailed information about a book.

    Parameters:
    - booksDict: Dictionary of book information
    - reviewsList: List of book reviews
    """
    print("Available books:")
    for i, title in enumerate(booksDict.keys(), start=1):
        print(f"{i}. {title}")

    while True:
        bookTitle = input("Please enter the title of the book: ").strip()
        if bookTitle in booksDict:
            booksValue = booksDict[bookTitle]
            print(
                f"\nTitle: {bookTitle}\nAuthor: {booksValue['author']}\nCategory: {booksValue['category']}\n\nDescription: {booksValue['description']}")
            print(
                f"\nPublisher: {booksValue['publisher']}\nYear: {booksValue['publishedDate']}")
            break
        else:
            print("Invalid book title. Please try again.")

    # Calculate average rating and price for the book
    reviewsForBook = [
        review for review in reviewsList if review[1] == bookTitle]
    if reviewsForBook:
        avgRating = sum(float(review[6])
                        for review in reviewsForBook) / len(reviewsForBook)
        avgPrice = sum(float(review[2])
                       for review in reviewsForBook) / len(reviewsForBook)
        print(f"Average Rating: {avgRating:.1f}")
        print(f"Average Price: ${avgPrice:.2f}")
    else:
        print("No reviews available for this book.")


def showAuthorRatings(booksDict: Dict[str, List[str]], reviewsList: List[List]) -> None:
    """
    Show average ratings for each author.

    Parameters:
    - booksDict: Dictionary of book information
    - reviewsList: List of book reviews
    """

    # I use defaultdict, which is also very useful dast scructure in python
    authorRatings: defaultdict[str, List[float]] = defaultdict(list)

    for review in reviewsList:
        # id, title, price, userId, profileName, helpfulness, score = review
        _, title, _, _, _, _, score = review
        author = booksDict[title]['author']
        authorRatings[author].append(float(score))
    for author, ratings in authorRatings.items():
        avgRating = sum(ratings) / len(ratings)
        print(f"Author: {author}, Average Rating: {avgRating:.1f}")


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
