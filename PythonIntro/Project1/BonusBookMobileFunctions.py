# Author: Hogan Lin
# Date: Oct 14th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Updated program using pandas for DataFrame processing.
#              And use several function to complete this menu-driven application 

import pandas as pd
import os


def loadBooks() -> pd.DataFrame:
    """
    Load a file containing a list of books using pandas.

    Returns:
    - DataFrame containing book information
    """
    while True:
        fileName = input("Please enter the name of the book file: ")
        if os.path.exists(fileName):
            break
        else:
            print(f"{fileName} does not exist.", end="")

    booksDf = pd.read_csv(fileName)
    print(booksDf)
    # Normalize categories to lowercase
    booksDf['categories'] = booksDf['categories'].str.lower()
    return booksDf


def loadReviews(booksDf: pd.DataFrame) -> pd.DataFrame:
    """
    Load a file containing a list of book reviews using pandas.

    Parameters:
    - booksDf: DataFrame of book information

    Returns:
    - DataFrame containing book reviews
    """
    while True:
        fileName = input("Please enter the name of the book reviews file: ")
        if os.path.exists(fileName):
            break
        else:
            print(f"{fileName} does not exist.", end="")

    reviewsDf = pd.read_csv(fileName)
    print(reviewsDf)

    # Error checking: Ensure all reviewed books exist in booksDf
    if not reviewsDf['Title'].isin(booksDf['Title']).all():
        raise LookupError(
            "Some reviewed books are not found in the book data.")

    return reviewsDf


def listBooksByCategory(booksDf: pd.DataFrame) -> None:
    """
    List all books within a literary category.

    Parameters:
    - booksDf: DataFrame of book information
    """
    categories = booksDf['categories'].unique()
    print("Available categories:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}: {category}")

    while True:
        category = input(
            "Which category of books would you like to see: ").strip().lower()
        if category in categories:
            break
        else:
            print(f"{category} is not a valid category.", end="")

    booksInCategory = booksDf[booksDf['categories'] == category]
    for i, row in booksInCategory.iterrows():
        print(f"\"{row['Title']}\" by {row['authors']}")
    print()


def showBookDetails(booksDf: pd.DataFrame, reviewsDf: pd.DataFrame) -> None:
    """
    Show detailed information about a book.

    Parameters:
    - booksDf: DataFrame of book information
    - reviewsDf: DataFrame of book reviews
    """
    print("\nAvailable books:")
    for i, title in enumerate(booksDf['Title'], start=1):
        print(f"{i}: {title}")

    while True:
        bookTitle = input(
            "Which book would you like to see the details of: ").strip()
        if bookTitle in booksDf['Title'].values:
            bookDetail = booksDf[booksDf['Title'] == bookTitle].iloc[0]
            print(f"\"{bookTitle}\" by {bookDetail['authors']}")
            print(bookDetail['description'])
            print(
                f"Published by {bookDetail['publisher']} in {bookDetail['publishedDate']}")
            print(f"Category: {bookDetail['categories']}")
            break
        else:
            print(f"{bookTitle} is not a valid book.", end="")

    # Calculate average rating and price for the book
    reviewsForBook = reviewsDf[reviewsDf['Title'] == bookTitle]
    if not reviewsForBook.empty:
        avgRating = reviewsForBook['review/score'].astype(float).mean()
        avgPrice = reviewsForBook['Price'].astype(float).mean()
        print(f"Price: ${avgPrice:.2f}")
        print(f"Average Rating: {avgRating:.1f}/5\n")
    else:
        print("No reviews available for this book.")


def showAuthorRatings(booksDf: pd.DataFrame, reviewsDf: pd.DataFrame) -> None:
    """
    Show average ratings for each author.

    Parameters:
    - booksDf: DataFrame of book information
    - reviewsDf: DataFrame of book reviews
    """
    mergedDf = pd.merge(booksDf, reviewsDf, on='Title', how='left')
    mergedDf['review/score'] = mergedDf['review/score'].astype(float)

    authorRatings = mergedDf.groupby(
        'authors')['review/score'].mean().fillna(0)

    for author, avgRating in authorRatings.items():
        if avgRating:
            print(f"{author}: {avgRating:.2f}/5")
        else:
            print(f"{author}: No Ratings")
    print()


def showHelpfulReviewer(reviewsDf: pd.DataFrame) -> None:
    """
    Show the name and average reviewHelpfulness rating of the most helpful reviewer.

    Parameters:
    - reviewsDf: DataFrame of book reviews
    """
    def calculateHelpfulness(helpfulness):
        numerator, denominator = map(int, helpfulness.split("/"))
        return numerator / denominator if denominator > 0 else 0

    def calculateHelpfulnessCount(helpfulness):
        return int(helpfulness.split("/")[0])

    reviewsDf['helpfulness'] = reviewsDf['review/helpfulness'].apply(
        calculateHelpfulness)
    reviewsDf['reviewCount'] = reviewsDf['review/helpfulness'].apply(
        calculateHelpfulnessCount)
    # copy reviewsDf avoid to pollute original data 
    reviewerStats = reviewsDf
    # remove the row if the review count less than 10
    reviewerStats = reviewerStats[reviewerStats['reviewCount'] >= 10]
    # get the highest row of the review/helpfulness point
    reviewerStats = reviewerStats.loc[reviewerStats['helpfulness'].idxmax()]
    if not reviewerStats.empty:
        mostHelpfulReviewer = reviewerStats['profileName']
        highestAvgHelpfulness = reviewerStats['helpfulness']
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
