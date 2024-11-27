class Node:
    def __init__(self,data):
        self.__data = data
        self.__next = None
        
    def getData(self):
        return self.__data
    
    def setData(self,data):
        self.__data = data

    def getNext(self):
        return self.__next

    def setNext(self,next):
        self.__next = next
        
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def append(self,data):
        temp = Node(data)

        if self.__head == None:
            self.__head = temp
        else:
            current = self.__head

            while current.getNext() != None:
                current = current.getNext()

            current.setNext(temp)

    def find(self,data):
        current = self.__head
        position = 0

        while current != None:
            if current.getData() == data:
                return position
            else:
                current = current.getNext()
                position += 1

        return -1

    def delete(self,data):
        if self.__head == None:
            return False
        elif self.__head.getData() == data:
            self.__head = self.__head.getNext()
            return True

        current = self.__head.getNext()
        previous = self.__head

        while current != None:
            if current.getData() == data:
                previous.setNext(current.getNext())
                return True
            else:
                previous = current
                current = current.getNext()

        return False

    def __str__(self):
        if self.__head == None:
            return "Empty"

        output = ""
        current = self.__head

        while current.getNext() != None:
            output += f"{current.getData()} -> "
            current = current.getNext()

        output += f"{current.getData()}"

        return output