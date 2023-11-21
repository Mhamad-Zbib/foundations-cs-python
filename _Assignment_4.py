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

        current.next = node
        node.next = current.next
        return f"Added node {value} at position {position}."
