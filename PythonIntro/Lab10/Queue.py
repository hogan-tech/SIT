# Author: Hogan Lin
# Date: Nov 25th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program implements a Queue data structure using a linked list. The Queue class
# provides basic operations like enqueue, dequeue, peek, clear.

class Node:
    """
    Represents a single node in the linked list, used as the building block for the queue.
    """
    def __init__(self, data):
        """
        Initializes a Node with the given data and sets the next pointer to None.
        :param data: The data to be stored in the node.
        :type data: Any
        """
        self.__data = data
        self.__next = None

    def getData(self):
        """
        Returns the data stored in the node.
        :return: The data in the node.
        :rtype: Any
        """
        return self.__data

    def setData(self, data):
        """
        Updates the data stored in the node.
        :param data: The new data to store in the node.
        :type data: Any
        """
        self.__data = data

    def getNext(self):
        """
        Returns the next node in the linked list.
        :return: The next node.
        :rtype: Node
        """
        return self.__next

    def setNext(self, next):
        """
        Updates the reference to the next node in the linked list.
        :param next: The next node to link to.
        :type next: Node
        """
        self.__next = next


class EmptyQueueException(Exception):
    """
    Custom exception for operations on an empty queue.
    """
    def __init__(self, action):
        """
        Initializes the exception with a message indicating the failed operation.
        :param action: The action attempted that caused the exception.
        :type action: str
        """
        message = f"Sorry, the queue is empty and we cannot {action}!"
        super().__init__(message)


class Queue:
    """
    Implements a Queue using a linked list.
    Supports operations like enqueue, dequeue, peek, and clear.
    """
    def __init__(self):
        """
        Initializes an empty queue with head and tail pointers set to None.
        """
        self.__head = None
        self.__tail = None

    def enqueue(self, data):
        """
        Adds a new element to the end of the queue.
        :param data: The data to be added to the queue.
        :type data: Any
        """
        new_node = Node(data)
        if self.__tail is None:  # If the queue is empty
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.setNext(new_node)
            self.__tail = new_node

    def dequeue(self):
        """
        Removes and returns the front element of the queue.
        :return: The data at the front of the queue.
        :rtype: Any
        :raises EmptyQueueException: If the queue is empty.
        """
        if self.__head is None:
            raise EmptyQueueException("dequeue")
        data = self.__head.getData()
        self.__head = self.__head.getNext()
        if self.__head is None:  # If the queue becomes empty
            self.__tail = None
        return data

    def peek(self):
        """
        Returns the front element of the queue without removing it.
        :return: The data at the front of the queue.
        :rtype: Any
        :raises EmptyQueueException: If the queue is empty.
        """
        if self.__head is None:
            raise EmptyQueueException("peek")
        return self.__head.getData()

    def clear(self):
        """
        Removes all elements from the queue.
        """
        self.__head = None
        self.__tail = None

    def __str__(self):
        """
        Returns a string representation of the queue, with elements separated by commas.
        :return: A comma-separated string of the queue's elements.
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
