# Author: Hogan Lin
# Date: Nov 25th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program implements a queue using a linked list. It reads queue operations 
# from an input file (inputQueue.txt), processes the operations (enqueue, dequeue, peek, clear, print).

def main():
    """
    Main function to handle queue operations based on input from a file.
    Reads operations such as enqueue, dequeue, peek, clear, and print from inputQueue.txt
    and performs them using the Queue class.
    """
    from Queue import Queue, EmptyQueueException  # Import custom Queue class and exception

    queue = Queue()  # Initialize an empty queue

    try:
        # Open the input file containing queue operations
        with open("./inputQueue.txt", "r") as file:
            for line in file:
                line = line.strip()  # Remove any leading/trailing whitespace
                if line.startswith("enqueue"):
                    # Handle the enqueue operation
                    _, value = line.split(maxsplit=1)  # Extract the value to be enqueued
                    queue.enqueue(value)
                    print(f"Enqueued {value}")
                elif line == "dequeue":
                    # Handle the dequeue operation
                    try:
                        value = queue.dequeue()
                        print(f"Dequeued {value}")
                    except EmptyQueueException as e:
                        print(e)  # Output exception message if queue is empty
                elif line == "peek":
                    # Handle the peek operation
                    try:
                        value = queue.peek()
                        print(f"Peeked at {value}")
                    except EmptyQueueException as e:
                        print(e)  # Output exception message if queue is empty
                elif line == "clear":
                    # Handle the clear operation
                    queue.clear()
                    print("Cleared out the queue.")
                elif line == "print":
                    # Handle the print operation
                    print(f"{queue}")
                else:
                    # Handle unknown operations
                    print(f"Unknown operation: {line}")
    except FileNotFoundError:
        # Handle case when input file is not found
        print("Error: inputQueue.txt not found.")

if __name__ == "__main__":
    main()
