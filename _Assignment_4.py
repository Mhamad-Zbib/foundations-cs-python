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
            return

        current = self.head
        count = 0
        while count < position - 1 and current.next is not None:
            current = current.next
            count += 1
