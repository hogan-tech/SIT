# Author: Hogan Lin
# Date: Jan 24th 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/Computing
# Note: Upload to github repo after deadline
# Description: calculating letter grades

def calculate(number_grade: float) -> str:
    """
    Convert numerical grade to letter grade.

    :param number_grade: Grade (0-100)
    :return: Letter grade ("A", "B", "C", "D", "F") or "N/A" if invalid
    """
    if not (0 <= number_grade <= 100):
        return "N/A"
    if number_grade < 60:
        return "F"
    if number_grade < 70:
        return "D"
    if number_grade < 80:
        return "C"
    if number_grade < 90:
        return "B"
    return "A"

