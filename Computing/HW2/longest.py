# Author: Hogan Lin
# Date: Jan 31st 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/Computing
# Note: Upload to GitHub repo after deadline
# Description: Finding the longest lines in a file

def longest_lines(filename: str) -> list:
    """
    Reads a file and returns all lines with the maximum length.

    :param filename: Name of the input file
    :return: List of longest lines (without trailing newlines)
    """
    with open(filename, "r") as file:
        lines = file.readlines()
    
    # use max method from hint1
    max_length = max(map(len, lines), default=0)
    return [line.strip() for line in lines if len(line) == max_length]
