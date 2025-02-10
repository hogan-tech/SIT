# Author: Hogan Lin
# Date: Feb 6th, 2025
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: Interactive program that prompts users for a letter 
# and tells its position in the alphabet.

def ordinal(n):
    """
    Converts a number into an ordinal representation (1st, 2nd, 3rd, etc.).

    :param n: The number to be converted
    :return: A string representing the ordinal form of the number
    """
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"

def main():
    """
    Interactive program that prompts users for a letter.
    Outputs the letter's position in the alphabet or exits on "stop".
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    while True:
        try:
            letter = input("Enter a letter: ").strip().lower()
            if letter == "stop":
                print("Goodbye.")
                break
            if len(letter) != 1:
                print("Please enter a single letter.")
                continue
            if letter not in alphabet:
                print("Please enter a letter from the English alphabet.")
                continue
            index = alphabet.index(letter) + 1
            print(f"'{letter}' is the {ordinal(index)} letter of the alphabet.")
        except (KeyboardInterrupt, EOFError):
            print("Goodbye.")
            break

# Run the program
if __name__ == "__main__":
    main()
