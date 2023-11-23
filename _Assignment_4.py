name = input("Enter your name: ")
print(f"Welcome {name.capitalize()}!")


def displayMenu():
    print(
        "the menu: \n"
        "       1. Singly Linked List \n"
        "       2. Check if Palindrome \n"
        "       3. Priority Queue \n"
        "       4. Evalualte an Infix Expression \n"
        "       5. Graph \n"
        "       6. Exit \n"
    )


class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, value, position):
        node = Node(value)

        if position == 0:
            node.next = self.head
            self.head = node
            return f"Added node {value} at position 0."

        current = self.head
        count = 0
        while count < position - 1 and current is not None:
            current = current.next
            count += 1

        if current is None:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            return f"Adding node {value} at the end of the LinkedList, since your position is out of bounds."

        node.next = current.next
        current.next = node
        return f"Added node {value} at position {position}."

    def displayNodes(self):
        current = self.head
        while current is not None:
            print(current.info, end=" => ")
            current = current.next
        return "None"

    def removeNode(self, value):
        current = self.head
        previous = None

        if current != None and current.info == value:
            self.head = current.next
            current = None
            return f"{value} is removed!"

        while current != None:
            if current.info == value:
                return f"{value} is removed!"
            previous = current
            current = current.next

        if current == None:
            return f"{value} was not found!"

        previous.next = current.next
        current = None


class Stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def isEmpty(self):
        return self.list == []

    def pop(self):
        if not self.isEmpty():
            return self.list.pop()
        else:
            return f"can't pop from an empty list!"


class Student():
    def __init__(self, name, midterm, final, attitude):
        self.name = name
        self.midterm = midterm
        self.final = final
        self.attitude = attitude
