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
        if self.head is None:
            self.head = node
            print(f"Adding {value} at first of the linkedlist since it was empty\n")
            return
        elif position == 0:
            node.next = self.head
            self.head = node
            print(f"Added node {value} at position {position}.\n")
            return
        current = self.head
        count = 0
        while current.next is not None and count < position - 1:
            current = current.next
            count += 1

        if count == position - 1:
            node.next = current.next
            current.next = node
            print(f"Added node {value} at position {position}.\n")
        else:
            current.next = node
            print(f"Added node {value} at the end of the LinkedList, since your position is out of bounds.\n")

    def displayNodes(self):
        current = self.head
        while current is not None:
            print(current.info, end=" => ")
            current = current.next
        print("None")

    def removeNode(self, value):
        current = self.head
        previous = None

        if current != None and current.info == value:
            self.head = current.next
            current = None
            print(f"{value} is removed!")
            return

        while current is not None:
            if current.info == value:
                print(f"{value} is removed!")
                break
            previous = current
            current = current.next
                

        if current == None:
            print(f"{value} was not found!")
            return

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


class Node1:
    def __init__(self, student):
        self.student = student
        self.next = None


class Student:
    def __init__(self, name, midterm, final, attitude):
        self.name = name
        self.midterm = midterm
        self.final = final
        self.attitude = attitude


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    def addStudent(self, student):
        node = Node1(student)
        if self.head == None:
            self.head = node
            self.size += 1
        else:
            current = self.head
            previous = None
            while current != None:
                if current.student.attitude == True and student.attitude == True:
                    if current.student.final > student.final:
                        previous = current
                        current = current.next
                    elif current.student.final == student.final:
                        if current.student.midterm > student.midterm:
                            previous = current
                            current = current.next
                        else:
                            break
                    else:
                        break
                elif current.student.attitude == False or student.attitude == False:
                    previous = current
                    current = current.next
                else:
                    if current.student.final > student.final:
                        previous = current
                        current = current.next
                    elif current.student.final == student.final:
                        if current.student.midterm > student.midterm:
                            previous = current
                            current = current.next
                        else:
                            break
                    else:
                        break

            if previous is None:
                node.next = self.head
                self.head = node
            elif previous is not None:
                node.next = current
                previous.next = node
            self.size += 1

    def interview(self):
        if self.size > 1:
            print(f"You have {self.size} more students to interview.")
            print(f"You have an interview now with: {self.head.student.name}\n")
            self.head = self.head.next
            self.size -= 1
            return self.interview()
        elif self.size == 1:
            print(f"You have {self.size} more student to interview.")
            print(f"You have an interview now with: {self.head.student.name}\n")
            self.head = self.head.next
            self.size -= 1
            return self.interview()
        elif self.size == 0 and self.head == None:
            print(f"Your interview list is empty.\n")


class InfixExpression:
    def operation(self, op, b, a):
        if op == "+":
            return a + b  
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b

    def priority(self, op):
        if op == "*" or op == "/":
            return 2
        elif op == "+" or op == "-":
            return 3
        elif op == "(" or op == ")":
            return 1
        else:
            return 0

    def evaluateString(self, expression):
        values = []  
        stack = []  
        i = 0
        while i < len(expression):
            if expression[i] == "":
                continue

            if expression[i] >= "0" and expression[i] <= "9":
                num = []
                if expression[i] >= "0" and expression[i] <= "9":
                    num.append(expression[i])
                    values.append(int(("".join(num))))

            elif expression[i] == "(":
                stack.append(expression[i])

            elif expression[i] == ")":
                if stack[-1] != "(":
                    values.append(self.operation(stack.pop(), values.pop(), values.pop()))  
                stack.pop()

            elif expression[i] == "*"or expression[i] == "/"or expression[i] == "+"or expression[i] == "-":
                stack.append(expression[i])

            i += 1

        while len(stack) != 0:
            values.append(self.operation(stack.pop(), values.pop(), values.pop()))
        return values


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def addVertex(self):
        self.num_vertices += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.num_vertices)
        print("Added vertex", self.num_vertices - 1, "\n")

    def addEdge(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1
            print(f"Added a vertex between vertices: {v1} and {v2} \n")

        elif (v1 < 0 or v1 >= self.num_vertices) and (v2 < 0 or v2 >= self.num_vertices):
            print(f"Invalid Vertices: {v1} and {v2} \n")

        elif v1 < 0 or v1 >= self.num_vertices:
            print(f"Invalid Vertex: {v1}")

        elif v2 < 0 or v2 >= self.num_vertices:
            print(f"Invalid Vertex: {v2}")

        elif (0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices) and v1 == v2:
            print("Invalid. Can't add same vertex.")

    def removeVertex(self, v):
        self.num_vertices -= 1
        self.adj_matrix.pop(v)
        for i in self.adj_matrix:
            self.adj_matrix.pop([i][v])
        print("Vertex removed with all edges connected to it.\n")

    def removeEdge(self, v1, v2):
        if self.adj_matrix[v1][v2] != 0 and self.adj_matrix[v2][v1] != 0:
            self.adj_matrix[v1][v2] = 0
            self.adj_matrix[v2][v1] = 0
        else:
            print(f"There is no edge between these vertices: {v1} and {v2}\n")

    def displayGraph(self, d):
        if len(self.adj_matrix) == 0:
            print("Graph is empty!\n")
            return
        for i in range(self.num_vertices):
            degree = sum(self.adj_matrix[i])
            if degree >= d:        
                print(f"Your vertex {i} has a degree of: {degree}.")



def first_choice_menu():
    print(
        "the menu: \n"
        "       a. Add Node \n"
        "       b. Display Nodes \n"
        "       c. Search for & Delete Node \n"
        "       d. Return to main menu \n"
    )


def main():
    choice = 0 
    while choice != 6:
        displayMenu()
        choice = input(" - Enter your choice: ")
        print()

        if choice == "":
            print(" - Try again and enter a number.")
        elif choice.isdigit():
            if int(choice) == 1:
                ll = LinkedList()
                while True:
                    first_choice_menu()
                    option = input(" - Enter which option you want to run in the Linked List: ")
                    print()
                    if option == "":
                        print(" - Try again and enter an option.\n")
                    if option.isdigit():
                        print(" - Try again and enter an option.\n")
                    elif option.lower() == "a":
                        value = int(input(" - Enter the value of the Node: "))
                        position = int(input(" - Enter the position of the Node: "))
                        print()
                        ll.addNode(value, position)
                    elif option.lower() == "b":
                        ll.displayNodes()
                        print()
                    elif option.lower() == "c":
                        value = int(input(" - Enter the value of the Node you want to remove: "))
                        print()
                        ll.removeNode(value)
                        print()
                    elif option.lower() == "d":
                        break
                    else:
                        print(" - Try again and enter a valid option.")
                        print()
            
            if int(choice) == 2:
                s = input(" - Enter a word to check if it's a palindrome: ")
                st = Stack()
                print()
                if s == "":
                    print(" - Try again and enter a word.\n")
                else:
                    for i in s:
                        st.push(i)

                    lst = ""
                    while not st.isEmpty():
                        lst += st.pop()

                    if lst == s:
                        print()
                        print(" - The word is a palindrome.\n")
                    else:
                        print()
                        print(" - The word is not a palindrome.\n")
                        print(s)
                        print(lst)  
                        print()

            if int(choice) == 3:
                pq = PriorityQueue()
                num = int(input("Enter how many students: "))
                for i in range(num):
                    name = input("Enter the name of the student: ")
                    midterm = int(input("Enter the midterm grade of the student: "))
                    final = int(input("Enter the final grade of the student: "))
                    attitude = input("Enter the attitude of the student (True or False): ")
                    print()
                    if attitude.lower() == "true":
                        attitude1 = True
                        student = Student(name.capitalize(), midterm, final, attitude1)
                        pq.addStudent(student)
                    elif attitude.lower() == "false":
                        attitude2 = False
                        student = Student(name.capitalize(), midterm, final, attitude2)
                        pq.addStudent(student)
                    else:
                        print("Try again and enter 'True' or 'False' for attitude.")
                pq.interview()

                


main()