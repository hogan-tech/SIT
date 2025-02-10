# Author: Hogan Lin
# Date: Feb 6th, 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Recursively prints a pyramid-like triangle.

def triangle(n, level=1):
    """
    Recursively generates a triangle pattern.

    :param n: Height of the triangle
    :param level: Current level (used for recursion)
    :return: A list of strings representing the triangle rows
    """
    if n == 0:
        return []
    rows = triangle(n - 1, level + 1)
    rows.append(" " * (level - 1) + "* " * (n - 1) + "*")
    return rows

def show_triangle(n):
    """
    Prints a right-aligned triangle of height n.

    :param n: Height of the triangle
    """
    print("\n".join(triangle(n)))

if __name__ == "__main__":
    show_triangle(5)
    show_triangle(3)
    show_triangle(1)
    show_triangle(0)
