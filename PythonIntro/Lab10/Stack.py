# Author: Hogan Lin
# Date: Nov 25th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program implements a Stack data structure using a linked list. 
# It includes operations such as push, pop, peek, and clear.

class Node:
    """
    Represents a single node in a linked list.
    """
    def __init__(self, data):
        """
        Initializes a Node with the provided data and sets the next pointer to None.
        :param data: The data to be stored in the Node.
        :type data: Any
        """
        self.__data = data
        self.__next = None

    def getData(self):
        """
        Returns the data stored in the Node.
        :return: The data stored in the Node.
        :rtype: Any
        """
        return self.__data

    def setData(self, data):
        """
        Updates the data stored in the Node.
        :param data: The new data to store.
        :type data: Any
        """
        self.__data = data

    def getNext(self):
        """
        Returns the next Node in the linked list.
        :return: The next Node.
        :rtype: Node
        """
        return self.__next

    def setNext(self, next):
        """
        Updates the reference to the next Node in the linked list.
        :param next: The next Node to link to.
        :type next: Node
        """
        self.__next = next


class EmptyStackException(Exception):
    """
    Custom exception for stack-related errors when the stack is empty.
    """
    def __init__(self, action):
        """
        Initializes the exception with a message explaining the issue.
        :param action: The action attempted that caused the exception.
        :type action: str
        """
        message = f"Sorry, the stack is empty and we cannot {action}!"
        super().__init__(message)


class Stack:
    """
    Implements a Stack data structure using a linked list.
    Supports standard stack operations like push, pop, peek, and clear.
    """
    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.__head = None

    def push(self, data):
        """
        Adds a new element to the top of the stack.
        :param data: The data to be added to the stack.
        :type data: Any
        """
        new_node = Node(data)
        new_node.setNext(self.__head)
        self.__head = new_node

    def pop(self):
        """
        Removes and returns the top element of the stack.
        :return: The data at the top of the stack.
        :rtype: Any
        :raises EmptyStackException: If the stack is empty.
        """
        if self.__head is None:
            raise EmptyStackException("pop")
        data = self.__head.getData()
        self.__head = self.__head.getNext()
        return data

    def peek(self):
        """
        Returns the top element of the stack without removing it.
        :return: The data at the top of the stack.
        :rtype: Any
        :raises EmptyStackException: If the stack is empty.
        """
        if self.__head is None:
            raise EmptyStackException("peek")
        return self.__head.getData()

    def clear(self):
        """
        Removes all elements from the stack.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the stack, with elements separated by commas.
        :return: A comma-delimited string of the stack's elements.
        :rtype: str
        """
        if self.__head is None:
            return ""
        current = self.__head
        elements = []
        while current is not None:
            elements.append(str(current.getData()))
            current = current.getNext()
        return ", ".join(elements)
