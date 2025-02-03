# Author: Hogan Lin
# Date: Jan 31st 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/Computing
# Note: Upload to GitHub repo after deadline
# Description: Summing positive numbers from input

import sys

def sum_positive_numbers() -> None:
    """
    Reads a single line of space-separated integers from stdin
    and prints the sum of all positive numbers.
    """
    numbers = map(int, sys.stdin.read().split())
    print(sum(n for n in numbers if n > 0))

if __name__ == "__main__":
    sum_positive_numbers()
