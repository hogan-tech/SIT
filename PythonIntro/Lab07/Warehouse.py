# Author: Hogan Lin
# Date: Nov 2nd 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This class represents a warehouse inventory system that allows the user to add and remove goods 
# while tracking the total number of goods stored. It includes methods to add goods, remove goods, and display 
# the current total inventory.

class Warehouse:
    def __init__(self, initialGoods=0):
        # Initialize the total amount of goods
        self.__totalGoods = initialGoods

    def addGoods(self):
        """
        Prompts the user to enter the number of goods to add to the warehouse,
        then increments the total goods by that amount.
        """
        amount = int(input("How many goods would you like to add: "))
        # Increment the total goods by the amount
        self.__totalGoods += amount

    def removeGoods(self):
        """
        Prompts the user to enter the number of goods to remove from the warehouse.
        Checks if there are enough goods to fulfill the request. If not, warns the user;
        otherwise, decrements the total goods by the specified amount.
        """
        amount = int(input("How many goods would you like to remove: "))
        # Check if the warehouse has enough goods to remove
        if amount > self.__totalGoods:
            print("You do not have that many goods!")
        else:
            # Decrement the total goods by the amount
            self.__totalGoods -= amount

    def get_totalGoods(self):
        print(f"There are {self.__totalGoods} goods in the warehouse.")
