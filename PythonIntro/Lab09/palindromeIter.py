# Author: Hogan Lin
# Date: Nov 17th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program checks whether a user-provided word is a palindrome using an iterative approach.
# It uses a loop to compare characters from both ends of the string and determines if the word is a palindrome.

def palindromeIter(word):
    """
    Function to determine if a word is a palindrome using iteration.
    :param word: The word to test.
    :type word: str
    :return: True if the word is a palindrome, False otherwise.
    :rtype: bool
    """
    # Loop through the string to check characters from both ends
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:  
            return False
    return True


def main():
    """
    Main function to get user input and check if the word is a palindrome.
    """
    # Prompt the user for input
    word = input("Please enter a word to test if it is a palindrome: ")

    if palindromeIter(word):
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome.")


# Call the main function
if __name__ == "__main__":
    main()
