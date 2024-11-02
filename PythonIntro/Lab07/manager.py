# Author: Hogan Lin
# Date: Nov 2nd 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program creates an interactive warehouse inventory tracker. It allows the user to
# add or remove goods from the warehouse and displays the total inventory of goods currently stored.
# The program runs in a loop until the user chooses to quit.

from Warehouse import Warehouse


def main():
    """
    Description: The main function of the warehouse inventory tracker. It creates an instance of the Warehouse class
    with an initial quantity of zero goods, displays a menu to the user, and handles user input to add or remove goods,
    display the total goods, or quit the program. Each menu option invokes the corresponding Warehouse method.
    """
    warehouse = Warehouse(0)

    while True:
        # Display menu options
        print("\nPlease select from the following options:")
        print("1: Add Goods")
        print("2: Remove Goods")
        print("3: Output Total Goods")
        print("4: Quit")

        choice = input("Choice: ")

        # Handle menu options with if-else
        if choice == "1":
            warehouse.addGoods()
        elif choice == "2":
            warehouse.removeGoods()
        elif choice == "3":
            warehouse.get_totalGoods()
        elif choice == "4":
            print("Good bye!")
            break
        else:
            print("Invalid choice, please select a valid option.")


if __name__ == "__main__":
    main()
