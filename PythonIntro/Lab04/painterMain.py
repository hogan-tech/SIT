# Author: Hogan Lin
# Date: Sept 30th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: create the program to input four option
# Input 1 to show ship, 2 to show cat, 3 to show piano, 4 to show gun
# Input other to show blank pattern with border
# Saperate to function and main files
import painterFuncs


def main():
    choice, border = painterFuncs.intro()

    if choice == 1:
        painterFuncs.sailingShip(border)
    elif choice == 2:
        painterFuncs.sleepingCat(border)
    elif choice == 3:
        painterFuncs.piano(border)
    elif choice == 4:
        painterFuncs.gun(border)
    else:
        painterFuncs.blank(border)
        print("Hmmmm....we don't seem to have that painting.")
        exit(-1)

    print("Hope you enjoyed your art!")


if __name__ == "__main__":
    main()
