# Author: Hogan Lin
# Date: Feb 27th 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/Computering
# Note: Upload to Gradescope before the deadline
# Description: Regular expression exercises for HW5

import re


def pequod(f: str) -> int:
    """
    Reads the contents of file f and returns the count of occurrences of 
    the phrase "white whale", ignoring space and capitalization.
    
    :param f: Filename
    :return: Count of occurrences of "white whale"
    """
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read().lower()
    return len(re.findall(r'\bwhite\s+whale(?:\'s)?\b', content))





def find_dotcoms(s):
    """
    Extracts domain names ending in ".com" from a string.
    Uses regular expressions.
    """
    # Match domain names ending in .com, ensuring no additional characters follow
    pattern = re.compile(r'\b([a-zA-Z0-9-]+)\.com\b(?!\.)')
    matches = pattern.findall(s)
    return matches


def palindrome_re(n: int) -> str:
    """
    Generates a regular expression that matches palindromes of length n.

    :param n: Length of the palindrome
    :return: Regular expression string
    """
    if n == 1:
        return r"."
    half = n // 2
    pattern = "".join([f"(.{{1}})" for _ in range(half)]) + (".?" if n %
                                                             2 else "") + "".join([f"\\{i}" for i in range(half, 0, -1)])
    return pattern


def palindrome_direct(s: str) -> bool:
    """
    Checks if a given string is a palindrome.

    :param s: Input string
    :return: True if s is a palindrome, False otherwise
    """
    return s == s[::-1]


# print(find_dotcoms("eff.org a.b.c.com www19.site.com bad.com.eu 1-2.3-4.comn"))
# r = palindrome_re(5)
# print(bool(re.fullmatch(r, 'abcba')))
# print(bool(re.fullmatch(r, 'abcbd')))
# print(bool(re.fullmatch(r, 'eeeee')))
# print(bool(re.fullmatch(r, 'racecar')))
# print(bool(re.fullmatch(r, '#. .#')))

# print(palindrome_direct('abcba'))
# print(palindrome_direct('abcbd'))
# print(palindrome_direct('eeeee'))
# print(palindrome_direct('racecar'))
# print(palindrome_direct(''))
# print(palindrome_direct('%^^%'))
