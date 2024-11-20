# Author: Hogan Lin
# Date: Nov 17th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program checks if a given series of parentheses is balanced using a recursive approach.
# It keeps track of counts using a global variable and validates the sequence for correctness.

# Global variable to keep track of the balance
count = 0


def parenthesis(parenthesisString, position):
    """
    Recursive function to check if the series of parentheses is balanced.
    :param parenthesisString: The string of parentheses to check.
    :type parenthesisString: str
    :param position: The current position in the string being checked.
    :type position: int
    :return: True if the parentheses are balanced, False otherwise.
    :rtype: bool
    """
    global count

    # Base case: End of string
    if position == len(parenthesisString):
        return count == 0  # True if all opened '(' are closed

    if parenthesisString[position] == '(':
        # Increment count for open parenthesis()
        count += 1
    elif parenthesisString[position] == ')':
        # Decrement count for close parenthesis
        count -= 1

        # If count goes negative, it means there are unmatched ')'
        if count < 0:
            return False

    return parenthesis(parenthesisString, position + 1)


def main():
    """
    Main function to get user input and check if the parentheses are balanced.
    """
    global count
    # Prompt the user for input
    parenString = input(
        "Please enter a series of parenthesis to see if they are balanced: ")

    # Reset the count before each new test
    count = 0

    # Call the recursive function and print the result
    if parenthesis(parenString, 0):
        print(f"{parenString} is balanced.")
    else:
        print(f"{parenString} is not balanced.")


# Call the main function
if __name__ == "__main__":
    main()
