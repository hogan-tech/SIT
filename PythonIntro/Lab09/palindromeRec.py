# Author: Hogan Lin
# Date: Nov 17th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program checks whether a user-provided word is a palindrome using a recursive approach.
# It demonstrates recursion with a base case for single or zero-length strings and recursive reduction.

def palindromeRec(word):
    """
    Function to determine if a word is a palindrome using recursion.
    :param word: The word to test.
    :type word: str
    :return: True if the word is a palindrome, False otherwise.
    :rtype: bool
    """
    # Base case: A single-character or empty string is a palindrome
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    # Recursive case: Check the substring excluding the first and last characters
    return palindromeRec(word[1:-1])

def main():
    """
    Main function to get user input and check if the word is a palindrome.
    """
    word = input("Please enter a word to test if it is a palindrome: ")
    
    # Call the palindrome test function
    if palindromeRec(word):
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome.")

# Call the main function
if __name__ == "__main__":
    main()
