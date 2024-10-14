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
            "Please enter the name of the book file: ")
        if os.path.exists(fileName):
            break
        else:
            print(f"{fileName} does not exist.", end="")

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
                "category": category.lower()
            }
            booksDict[title] = bookDetail
            categoriesSet.add(category.lower())

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
            "Please enter the name of the book reviews file: ")
        if os.path.exists(fileName):
            break
        else:
            print(f"{fileName} does not exist.", end="")

    with open(fileName, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            line = line.strip()
            id, title, price, userId, profileName, reviewHelpfulness, score = line.split(
                ",")
            if title not in booksDict:
                raise LookupError(
                    f"Book '{title}' not found in the book dictionary.")
            reviewsList.append(
                [id, title, price, userId, profileName, reviewHelpfulness, score])

    return reviewsList


def listBooksByCategory(booksDict: Dict[str, List[str]], categoriesSet: Set[str]) -> None:
    """
    List all books within a literary category.

    Parameters:
    - booksDict: Dictionary of book information
    - categoriesSet: Set of literary categories
    """
    print("Available categories:")
    for i, category in enumerate(categoriesSet, start=1):
        print(f"{i}: {category}")

    while True:
        category = input(
            "Which category of books would you like to see: ").strip().lower()
        if category in categoriesSet:
            break
        else:
            print(
                f"{category} is not a valid category.", end="")
    for i, (_, booksValue) in enumerate(booksDict.items(), start=1):
        if booksValue['category'] == category:
            print(f"\"{booksValue['title']}\" by {booksValue['author']}")
    print()


def showBookDetails(booksDict: Dict[str, List[str]], reviewsList: List[List]) -> None:
    """
    Show detailed information about a book.

    Parameters:
    - booksDict: Dictionary of book information
    - reviewsList: List of book reviews
    """
    print("\nAvailable books:")
    for i, title in enumerate(booksDict.keys(), start=1):
        print(f"{i}: {title}")

    while True:
        bookTitle = input(
            "Which book would you like to see the details of: ").strip()
        if bookTitle in booksDict:
            booksValue = booksDict[bookTitle]
            print(f"\"{bookTitle}\" by {booksValue['author']}")
            print(booksValue['description'])
            print(
                f"Published by {booksValue['publisher']} in {booksValue['publishedDate']}")
            print(f"Category: {booksValue['category']}")
            break
        else:
            print(f"{bookTitle} is not a valid book.", end="")

    # Calculate average rating and price for the book
    reviewsForBook = [
        review for review in reviewsList if review[1] == bookTitle]
    if reviewsForBook:
        avgRating = sum(float(review[6])
                        for review in reviewsForBook) / len(reviewsForBook)
        avgPrice = sum(float(review[2])
                       for review in reviewsForBook) / len(reviewsForBook)
        print(f"Price: ${avgPrice:.2f}")
        print(f"Average Rating: {avgRating:.1f}/5\n")
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
    titleSet = set()

    for title in booksDict.keys():
        titleSet.add(title)

    for review in reviewsList:
        # id, title, price, userId, profileName, reviewHelpfulness, score = review
        _, title, _, _, _, _, score = review
        author = booksDict[title]['author']
        if title in titleSet:
            titleSet.remove(title)
        if ";" in author:
            for newAuthor in author.split(";"):
                authorRatings[newAuthor].append(float(score))
        else:
            authorRatings[author].append(float(score))
    for remainTitle in titleSet:
        author = booksDict[remainTitle]['author']
        if ";" in author:
            for newAuthor in author.split(";"):
                authorRatings[newAuthor].append(float(0))
        elif author not in authorRatings:
            authorRatings[author].append(float(0))

    for author, ratings in authorRatings.items():
        avgRating = sum(ratings) / len(ratings)
        if avgRating:
            print(f"{author}: {avgRating:.2f}/5")
        else:
            print(f"{author}: No Ratings")
    print()


def showHelpfulReviewer(reviewsList: List[List]) -> None:
    """
    Show the name and average reviewHelpfulness rating of the most helpful reviewer.

    Parameters:
    - reviewsList: List of book reviews
    """
    reviewerData = defaultdict(lambda: [0, 0])
    # {reviewerName: [totalHelpful, totalReviewed]}

    for review in reviewsList:
        _, _, _, _, profileName, reviewHelpfulness, _ = review
        numerator, denominator = map(int, reviewHelpfulness.split("/"))

        if denominator > 0:
            reviewerData[profileName][0] += numerator
            reviewerData[profileName][1] += denominator

    mostHelpfulReviewer = ""
    highestAvgHelpfulness = 0
    for profileName, (totalHelpful, totalReviewed) in reviewerData.items():
        if totalReviewed >= 10:
            avgHelpfulness = totalHelpful / totalReviewed
            if avgHelpfulness > highestAvgHelpfulness:
                highestAvgHelpfulness = avgHelpfulness
                mostHelpfulReviewer = profileName

    if mostHelpfulReviewer:
        print(
            f"The most helpful reviewer was {mostHelpfulReviewer} with an average rating of {int(highestAvgHelpfulness * 100)}% helpful!\n")
    else:
        print("No reviewer with sufficient reviews.")


def welcome() -> None:
    print("Welcome to the Book Mobile! We have many books to offer. Please choose from the following menu of options!")


def goodBye() -> None:
    print("Thank you for visiting the Book Mobile!")


def menu() -> int:
    """
    Show a menu and get the user's choice.

    Returns:
    - int: The number of the option the user chose
    """
    print("1. Load Book File")
    print("2. Load Review File")
    print("3. Books by Category")
    print("4. Book Details")
    print("5. Author Average Ratings")
    print("6. Most Helpful Reviewer")
    print("7. Quit")
    choice = input("Please enter a choice (1-7): ")

    return int(choice)
