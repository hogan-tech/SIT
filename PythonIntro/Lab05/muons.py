# Author: Hogan Lin
# Date: Oct 6th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program simulates an 8x8 array (map) of cosmic ray muon detector (CRMD)
#              capture rates. Each cell in the map represents a randomly generated capture rate
#              between 0 and 500. The program finds and outputs the highest and lowest capture rates,
#              along with their coordinates in the grid. It also displays the entire grid of capture rates.

"""
The main function creates an 8x8 map of random capture rates, finds the highest and lowest 
rates along with their coordinates, and then displays the map in a grid format.

:return: None. Prints the map and results to the console.
"""

import random
from typing import List, Tuple


SIZE = 8


def createMap() -> List[List[int]]:
    """
    Creates an 8x8 map with random capture rates between 0 and 500.

    :return: A two-dimensional list (8x8) with random integers between 0 and 500.
    :rtype: List[List[int]]
    """
    muonMap = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            muonMap[i][j] = random.randint(0, 500)

    return muonMap


def findHighestLowestCapture(muonMap: List[List[int]]) -> Tuple[int, Tuple[int, int], int, Tuple[int, int]]:
    """
    Finds the highest and lowest capture rates in the muon map, along with their coordinates.

    :param muonMap: A two-dimensional list (8x8) containing capture rates.
    :type muonMap: List[List[int]]
    :return: A tuple containing the highest capture rate, its coordinates (x, y), 
             the lowest capture rate, and its coordinates (x, y). Coordinates are 
             adjusted to be human-friendly (starting from 1 instead of 0).
    :rtype: Tuple[int, Tuple[int, int], int, Tuple[int, int]]
    """
    highestRate = -1
    lowestRate = 501
    highestX, highestY = 0, 0
    lowestX, lowestY = 0, 0

    for i in range(SIZE):
        for j in range(SIZE):
            currentRate = muonMap[i][j]
            if currentRate > highestRate:
                highestRate = currentRate
                highestX, highestY = i, j
            if currentRate < lowestRate:
                lowestRate = currentRate
                lowestX, lowestY = i, j

    return highestRate, (highestX + 1, highestY + 1), lowestRate, (lowestX + 1, lowestY + 1)


def printMap(muonMap: List[List[int]]) -> None:
    """
    Prints the 8x8 muon map in a grid format for easy reading.

    :param muonMap: A two-dimensional list (8x8) containing capture rates.
    :type muonMap: List[List[int]]
    :return: None. Prints the map to the console.
    """

    for row in muonMap:
        for val in row:
            print(f"{val:4}", end=" ")
        print()


def main():
    """
    Main function to drive the program. It creates the muon map, finds the highest and lowest 
    capture rates, and prints the results and map.

    :return: None. Prints results to the console.
    """
    muonMap = createMap()

    highestRate, highestCoords, lowestRate, lowestCoords = findHighestLowestCapture(
        muonMap)

    print(
        f"The highest capture rate was {highestRate} at location {highestCoords[0]},{highestCoords[1]}.")
    print(
        f"The lowest capture rate was {lowestRate} at location {lowestCoords[0]},{lowestCoords[1]}.")

    print("\nThe map looks like the following:")
    printMap(muonMap)


if __name__ == "__main__":
    main()
