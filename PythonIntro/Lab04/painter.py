# Author: Hogan Lin
# Date: Sept 30th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: create the program to input four option
# Input 1 to show ship, 2 to show cat, 3 to show piano, 4 to show gun
# Input other to show blank pattern with border
def intro():
    print("Welcome to the painting printer!")
    print("We have many options:")
    print("1. The S.S. Satisfaction")
    print("2. Mina in Repose")
    print("3. The Piano")
    print("4. The Gun")

    choice = int(input("Please select a painting to print: "))
    border = input("What border would you like around your painting: ")

    return choice, border


def printHeaderFooter(border, size):
    print(border * (size + 2))


def sleepingCat(border):
    art = [
        "      |\\      _,,,---,,_      ",
        "ZZZzz /,`.-'`'    -.  ;-;;,_  ",
        "     |,4-  ) )-,_. ,\\ (  `'-' ",
        "    '---''(_/--'  `-'\\_)      "
    ]

    size = len(art[0]) + 2
    printHeaderFooter(border, size)
    for line in art:
        print(f"{border} {line} {border}")
    printHeaderFooter(border, size)


def sailingShip(border):
    art = [
        "      |    |    |           ",
        "     )_)  )_)  )_)          ",
        "    )___))___))___)\\        ",
        "   )____)____)_____)\\\\      ",
        " _____|____|____|____\\\\\\__  ",
        " \\    Satisfaction   /      ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    ]

    size = len(art[0]) + 2
    printHeaderFooter(border, size)
    for line in art:
        print(f"{border} {line} {border}")
    printHeaderFooter(border, size)


def piano(border):
    art = [
        "_______",
        "|_____|",
        "|=====|",
        "|--w--|"
    ]

    size = len(art[0]) + 2
    printHeaderFooter(border, size)
    for line in art:
        print(f"{border} {line} {border}")
    printHeaderFooter(border, size)


def gun(border):
    art = [
        "+--^----------,--------,-----,--------^-,",
        "| |||||||||   `--------'     |          O",
        "`+---------------------------^----------|",
        "  `\_,---------,---------,--------------'",
        "    / XXXXXX /'|       /'                ",
        "   / XXXXXX /  `\    /'                  ",
        "  / XXXXXX /`-------'                    ",
        " / XXXXXX /                              ",
        "/ XXXXXX /                               ",
        "(________(                               ",
        "`------'                                 "
    ]

    size = len(art[0]) + 2
    printHeaderFooter(border, size)
    for line in art:
        print(f"{border} {line} {border}")
    printHeaderFooter(border, size)


def blank(border):
    size = 7
    printHeaderFooter(border, size)
    for _ in range(5):
        print(f"{border}       {border}")
    printHeaderFooter(border, size)


def main():
    choice, border = intro()

    if choice == 1:
        sailingShip(border)
    elif choice == 2:
        sleepingCat(border)
    elif choice == 3:
        piano(border)
    elif choice == 4:
        gun(border)
    else:
        blank(border)
        print("Hmmmm....we don't seem to have that painting.")
        exit(-1)

    print("Hope you enjoyed your art!")


if __name__ == "__main__":
    main()
