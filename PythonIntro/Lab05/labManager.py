# Author: Hogan Lin
# Date: Oct 6th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program manages a small laboratory's equipment inventory.
#              The lab can store up to five pieces of equipment at a time.
#              Users can add, remove, and display current equipment, or leave the laboratory manager.
#              The program continues running until the user opts to exit.

"""
The labManager function is the main driver of the program, allowing the user to interact with 
the laboratory equipment inventory. It displays a menu and prompts the user to choose actions.

:param None: The function does not take any parameters.
:return: None. It handles user inputs and prints outputs based on user actions.
"""


from typing import List


def displayMenu():
    """
    Prints the menu options for the user to interact with the laboratory inventory.

    :param None: No parameters.
    :return: None. Displays menu options.
    """

    print("\nYou can choose from the following options:")
    print("1. Add Equipment")
    print("2. Remove Equipment")
    print("3. Display Current Equipment")
    print("4. Leave the Laboratory Manager")


def addEquipment(labEquipment: List[str]):
    """
    Adds a new equipment item to the lab, provided it doesn't exceed the 5-item limit.

    :param labEquipment: List of strings representing the current lab equipment.
    :type labEquipment: List[str]
    :return: None. Updates the equipment list and prints a success or error message.
    """

    if len(labEquipment) >= 5:
        print("You cannot add more equipment. The laboratory is full!")
    else:
        equipment = input("What would you like to add to the laboratory: ")
        labEquipment.append(equipment)
        print(f"{equipment} has been added")


def removeEquipment(labEquipment: List[str]):
    """
    Removes an equipment item from the lab, if it exists in the list.

    :param labEquipment: List of strings representing the current lab equipment.
    :type labEquipment: List[str]
    :return: None. Updates the equipment list and prints a success or error message.
    """

    equipment = input("What would you like to remove from the laboratory: ")
    if equipment in labEquipment:
        labEquipment.remove(equipment)
        print(f"{equipment} has been removed")
    else:
        print(f"{equipment} was not present and could not be removed")


def displayEquipment(labEquipment: List[str]):
    """
    Displays the current equipment in the laboratory.

    :param labEquipment: List of strings representing the current lab equipment.
    :type labEquipment: List[str]
    :return: None. Prints the list of equipment or a message if the lab is empty.
    """

    if not labEquipment:
        print("The laboratory is currently empty.")
    else:
        print("Your laboratory currently contains: ")
        for item in labEquipment:
            print(item, end=" ")
        print()  


def labManager():
    """
    The main function that manages the interaction with the laboratory equipment inventory.
    It runs a loop until the user chooses to exit and allows them to add, remove, or view equipment.

    :param None: No parameters.
    :return: None. Runs the lab management process.
    """

    labEquipment: List[str] = []

    print("Welcome to the inventory manager for your laboratory!")

    while True:
        displayMenu()
        choice: str = input("What would you like to do: ")

        if choice == "1":
            addEquipment(labEquipment)
        elif choice == "2":
            removeEquipment(labEquipment)
        elif choice == "3":
            displayEquipment(labEquipment)
        elif choice == "4":
            print("Good luck on your journey of discovery!")
            break
        else:
            print(f"{choice} was not a valid option. Please try again")


labManager()

"""
input
1
Telescope
1
Electron Microscope
1
Electromagnets
1
Liquid Helium
1
Lenses
1
2
Telescope
2
Telescope
3
5
4
"""
