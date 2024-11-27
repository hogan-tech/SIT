# Author: Hogan Lin
# Date: Nov 25th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program implements a stack using a linked list. It reads stack operations from
# an input file (inputStack.txt), processes the operations (push, pop, peek, clear, print), and 
# outputs the results to the console.

def main():
    """
    Main function to handle stack operations based on input from a file.
    Reads operations such as push, pop, peek, clear, and print from inputStack.txt
    and performs them using the Stack class.
    """
    from Stack import Stack, EmptyStackException  # Import custom Stack class and exception

    stack = Stack()  # Initialize an empty stack

    try:
        # Open the input file containing stack operations
        with open("./inputStack.txt", "r") as file:
            for line in file:
                line = line.strip()  # Remove any leading/trailing whitespace
                if line.startswith("push"):
                    # Handle the push operation
                    _, value = line.split()  # Extract the value to be pushed
                    stack.push(int(value))
                    print(f"Pushed {value}")
                elif line == "pop":
                    # Handle the pop operation
                    try:
                        value = stack.pop()
                        print(f"Popped {value}")
                    except EmptyStackException as e:
                        print(e)  # Output exception message if stack is empty
                elif line == "peek":
                    # Handle the peek operation
                    try:
                        value = stack.peek()
                        print(f"Peeked at {value}")
                    except EmptyStackException as e:
                        print(e)  # Output exception message if stack is empty
                elif line == "clear":
                    # Handle the clear operation
                    stack.clear()
                    print("Cleared out the stack.")
                elif line == "print":
                    # Handle the print operation
                    print(f"{stack}")
                else:
                    # Handle unknown operations
                    print(f"Unknown operation: {line}")
    except FileNotFoundError:
        # Handle case when input file is not found
        print("Error: inputStack.txt not found.")

if __name__ == "__main__":
    main()
