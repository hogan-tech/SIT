# Author: Hogan Lin
# Date: Nov 17th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program calculates the result of a user-specified base value raised to a user-specified exponent.
# It uses a recursive function to compute the result and demonstrates the use of recursion through printed output.

def powers(base, exponent):
    """
    Recursive function to calculate base raised to the power of exponent.
    :param base: The base value (integer).
    :type base: int
    :param exponent: The exponent value (integer).
    :type exponent: int
    :return: The result of base raised to the power of exponent.
    :rtype: int
    """
    print(f"powers({base},{exponent})")
    if exponent == 1:
        return base
    return base * powers(base, exponent - 1)


def main():
    """
    Main function to get user input and calculate the result of base raised to the power of exponent.
    """
    # Prompt the user for input
    base = int(input("Please enter the base value: "))
    exponent = int(input("Please enter the exponent value: "))

    result = powers(base, exponent)

    print(f"{base}^{exponent} is {result}")


if __name__ == "__main__":
    main()
