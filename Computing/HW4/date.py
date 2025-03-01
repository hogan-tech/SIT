# Author: Hogan Lin
# Date: Feb 19th 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/Computing
# Description: Date class implementation with doctests
class Date:

    def __init__(self, year: int, month: int, day: int):
        """Initialize a Date object."""
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        """Return a string representation for debugging."""
        return f"Date({self.year}, {self.month}, {self.day})"

    def __str__(self):
        """Return a formatted string representation of the date."""
        return f"{self.month:02}/{self.day:02}/{self.year:04}"

    def is_leap_year(self) -> bool:
        """
        Determines if the year is a leap year.

        >>> Date(2020, 1, 1).is_leap_year()
        True
        >>> Date(1900, 1, 1).is_leap_year()
        False
        """
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            return True
        return False

    def is_valid(self) -> bool:
        """
        Determines if the date is valid.

        >>> Date(2021, 2, 29).is_valid()
        False
        >>> Date(2020, 2, 29).is_valid()
        True
        """
        days_in_month = [0, 31, 28 + self.is_leap_year(), 31,
                         30, 31, 30, 31, 31, 30, 31, 30, 31]
        return 1 <= self.month <= 12 and 1 <= self.day <= days_in_month[self.month] and self.year != 0

    def tomorrow(self):
        """
        Advances the date by one day.

        >>> d = Date(2021, 11, 8)
        >>> d.tomorrow()
        >>> d
        Date(2021, 11, 9)
        >>> d = Date(2020, 12, 31)
        >>> d.tomorrow()
        >>> d
        Date(2021, 1, 1)
        """
        days_in_month = [0, 31, 28 + self.is_leap_year(), 31,
                         30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.day < days_in_month[self.month]:
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1



d = Date(2021, 11, 8)
print(d)
print(str(d))
print(repr(d))
d2 = Date(1776, 7, 4)
print(d2)
d3 = Date(76, 1, 24)
print(d3)