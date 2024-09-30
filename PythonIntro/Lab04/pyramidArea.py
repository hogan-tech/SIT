# Author: Hogan Lin
# Date: Sept 30th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: In this exercise, we need to create three functions to calculate surface area
import math


def calcBaseArea(side: float):
    # Calculate base area
    return side ** 2


def calcSideArea(side: float, height: float):
    # Calculate the side area depend on the equation
    return 2 * side * math.sqrt((side ** 2) / 4 + height ** 2)


def prntSurfArea(side: float, height: float):
    # Calculate the total surface area and print out
    totalArea = calcBaseArea(side) + calcSideArea(side, height)
    print(
        f"The total surface area of the square pyramid is {totalArea} square feet.")


def main():
    side = float(
        input("Enter the side length of the base of the square pyramid in feet: "))

    height = float(input("Enter the height of the square pyramid in feet: "))

    baseArea = calcBaseArea(side)
    print(
        f"Base surface area of the square pyramid is {baseArea} square feet.")

    # add your function to calculate the side area and assign
    sideArea = calcSideArea(side, height)
    # the result to side_area, then print the result
    print(
        f"Total surface area of all four sides of the square pyramid is {sideArea} square feet.")
    # add your function call to print the total surface area
    prntSurfArea(side, height)


if __name__ == "__main__":
    main()
