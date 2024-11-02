# Author: Hogan Lin
# Date: Nov 2nd 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This file defines the Product class, which encapsulates data and functionality 
# related to a product order, including attributes for name, units, price per unit, 
# and total cost. The class provides getter and setter methods to manipulate each attribute.



class Product:
    def __init__(self, name="", units=0, price=0.0):
        self.__name = name
        self.__units = units
        self.__price = price
        self.__totalCost = 0.0

    # Getter for product name
    def get_name(self):
        return self.__name

    # Setter for product name
    def set_name(self, name):
        self.__name = name

    # Getter for units
    def get_units(self):
        return self.__units

    # Setter for units
    def set_units(self, units):
        self.__units = units

    # Getter for price
    def get_price(self):
        return self.__price

    # Setter for price
    def set_price(self, price):
        self.__price = price

    # Getter for total cost
    def get_totalCost(self):
        return self.__totalCost

    # Setter for total cost
    def set_totalCost(self, totalCost):
        self.__totalCost = totalCost
