# Author: Hogan Lin
# Date: Nov 2nd 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Defines the SmartProduct class, which represents a product with attributes 
# like ID, name, quantity, unit price, and total cost. Provides methods to manage 
# product details and automatically updates the total cost when quantity or price changes.


class SmartProduct:
    def __init__(self, productId, name, units, pricePerUnit):
        # Initialize all private variables
        self.__productId = productId
        self.__name = name
        self.__units = units
        self.__pricePerUnit = pricePerUnit
        self.__totalCost = self.__units * self.__pricePerUnit

    # Getter and setter for product ID
    def get_productId(self):
        return self.__productId

    def set_productId(self, productId):
        self.__productId = productId

    # Getter and setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and setter for units
    def get_units(self):
        return self.__units

    def set_units(self, units):
        self.__units = units
        # Update total cost whenever units are set
        self.__totalCost = self.__units * self.__pricePerUnit

    # Getter and setter for price per unit
    def get_pricePerUnit(self):
        return self.__pricePerUnit

    def set_pricePerUnit(self, pricePerUnit):
        self.__pricePerUnit = pricePerUnit
        # Update total cost whenever price per unit is set
        self.__totalCost = self.__units * self.__pricePerUnit

    # Getter for total cost
    def get_totalCost(self):
        return self.__totalCost
