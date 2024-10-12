# Author: Hogan Lin
# Date: Oct 11th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program reads integer values from a file named 'numbers.txt',
#              calculates the average of the numbers, and prints both the numbers
#              and the computed average to the screen. The file is processed line
#              by line, and non-numeric lines are ignored. If the file does not exist,
#              an error message is displayed.


def main():
    """
    This main function reads integers from a file, prints each integer, and calculates the average.
    """
    try:
        with open('./numbers.txt', 'r') as file:
            total = 0
            count = 0

            for line in file:
                line = line.strip()
                if line.isdigit():
                    number = int(line)
                    print(number)
                    total += number
                    count += 1

            if count > 0:
                average = total / count
                print(f"The average of the numbers is {average}")
            else:
                print("No numbers to calculate an average.")

    except FileNotFoundError:
        print("The file 'numbers.txt' was not found.")


if __name__ == "__main__":
    main()
