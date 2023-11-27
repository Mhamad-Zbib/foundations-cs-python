name = input("Enter your name: ")
print(f"Welcome {name.capitalize()}!")


def displayMenu(): # O(1)
    # The Main Menu
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

    def addNode(self, value, position): # O(N), N being the length of the Nodes.
        # In this LinkedList, the user is able to add a node and if the node is empty then the head will point to the new node.
        # And if the user enters a position out of bounds it will add it to the end of the LL.
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

    def displayNodes(self): # O(N), N being the length of the Nodes.
        # The user is able to display the nodes.
        current = self.head
        while current is not None:
            print(current.info, end=" => ")
            current = current.next
        print("None")

    def removeNode(self, value): # O(N), N being the length of the Nodes.
        # In this function after the user insert the value he wants to remove the function will search for thev value and remove it. However, it will only remove the value once.
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
    def __init__(self): # O(1)
        # Initializing an empty list.
        self.list = []

    def push(self, data): # O(1)
        # Appending elemetns insite the list.
        self.list.append(data)

    def isEmpty(self): # O(1)
        # Check if the list is empty
        return self.list == []

    def pop(self): # O(1)
        # Remove the last element from the list if the list is not empty.
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
        # Initializing the student class.
        self.name = name
        self.midterm = midterm
        self.final = final
        self.attitude = attitude


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    def addStudent(self, student): # O(N), N being the length of the Node.
        # add a student to the priority queue, at first will interview the student with good attitude.
        # Second the student with the highest final grade.
        # Third the student with the highest midterm grade.
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

    def interview(self): # O(1)
        # In this functon, the HR will interview the students. Based on the size of the Priority Queue(students) and by order.
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
    def operation(self, op, b, a): # O(1)
        # In this function, we let each operator to perform operations on values.
        if op == "+":
            return a + b  
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b

    def priority(self, op): # O(1)
        # Here we give priority based on the order of operations PEMDAS.
        if op == "*" or op == "/":
            return 2
        elif op == "+" or op == "-":
            return 1
        elif op == "(" or op == ")":
            return 0
        else:
            return -1

    def evaluateString(self, expression): # O(N), N Being the length of the list
        # In this function we use 2 stacks to store operators and numbers and then the function will evaluate them at the end.
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
        # In this graph i used the adjacency matrix since the user is allowed to insert as many edges as he wants and to make the graph dense.
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def addVertex(self): # O(V). 
        # This function permits the user to add a vertex(row).
        self.num_vertices += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.num_vertices)
        print("Added vertex", self.num_vertices, "\n")

    def addEdge(self, v1, v2): # O(1)
        # In here the function will add an edge between to vertices.
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1
            print(f"Added an edge between vertices: {v1} and {v2} \n")

        elif (v1 < 0 or v1 >= self.num_vertices) and (v2 < 0 or v2 >= self.num_vertices):
            print(f"Invalid Vertices: {v1} and {v2} \n")

        elif v1 < 0 or v1 >= self.num_vertices:
            print(f"Invalid Vertex: {v1}")

        elif v2 < 0 or v2 >= self.num_vertices:
            print(f"Invalid Vertex: {v2}")


    def removeVertex(self, v): # O(V).
        # The function will remove the vertex and all edges connected to it.
        if v < 0 or v >= self.num_vertices:
            print("Invalid index to remove.")
            return 
        self.num_vertices -= 1
        self.adj_matrix.pop(v)
        for i in self.adj_matrix:
            i.pop(v)
        print("Vertex removed with all edges connected to it.\n")

    def removeEdge(self, v1, v2): # O(1)
        # in here the user will remove an edge between to vertices.
        if self.adj_matrix[v1][v2] != 0 and self.adj_matrix[v2][v1] != 0:
            self.adj_matrix[v1][v2] = 0
            self.adj_matrix[v2][v1] = 0
            print(f"Edge between {v1} and {v2} is removed. \n")
        else:
            print(f"There is no edge between these vertices: {v1} and {v2}\n")

    def displayGraph(self, d): # O(V).
        # In here the function will display the graph based on the degree he inserts, all vertices containing that degree will be displayed.
        if len(self.adj_matrix) == 0:
            print("Graph is empty!\n")
            return
        for i in range(self.num_vertices):
            degree = sum(self.adj_matrix[i])
            if degree >= d:        
                print(f"Your vertex {i} has a degree of: {degree}.")



def first_choice_menu(): # O(1)
    # Menu of the Linked List
    print(
        "the menu: \n"
        "       a. Add Node \n"
        "       b. Display Nodes \n"
        "       c. Search for & Delete Node \n"
        "       d. Return to main menu \n"
    )

def fifth_choice_menu(): # O(1)
        # Menu of the graph
        print(
        "the menu: \n"
        "       a. Add Vertex \n"
        "       b. Add Edge \n"
        "       c. Remove Vertex \n"
        "       d. Remove Edge \n"
        "       e. Display Vertices With a Degree of X or more \n"
        "       f. Return to Main Menu\n"
    )
        


def main(): # O(N^2), N being the size of input.
    choice = 0
    consecutive_errors = 0
    while choice != 6:
        displayMenu()
        choice = input(" - Enter your choice: ")
        print()

        if choice == "":
            print(" - Try again and enter a number.\n")
            consecutive_errors += 1
        elif not choice.isdigit():
            print(" - Try again and enter a valid number.\n")
            consecutive_errors += 1
        elif int(choice) < 1 or int(choice) > 6:
            print(" - Try again and choose a number between 1 and 6.\n")
            consecutive_errors += 1
        else:
            consecutive_errors = 0
        
        if consecutive_errors >=4:
            print(" - To many consecutive errors. Exiting.")
            break

        if choice.isdigit():
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
            
            elif int(choice) == 2:
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

            elif int(choice) == 3:
                pq = PriorityQueue()
                num = int(input(" - Enter how many students: "))
                for i in range(num):
                    name = input(" - Enter the name of the student: ")
                    midterm = int(input(" - Enter the midterm grade of the student: "))
                    final = int(input(" - Enter the final grade of the student: "))
                    attitude = input(" - Enter the attitude of the student (True or False): ")
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
                        print(" - Try again and enter 'True' or 'False' for attitude.")
                pq.interview()

            elif int(choice) == 4:
                infix = InfixExpression()
                expression = input(" - Enter your expression: ")
                result = infix.evaluateString(expression)
                print(f" - Result: {result}")

            elif int(choice) == 5:
                num = input(" - Enter the number of vertices: ")
                print()
                if num == "":
                    print(" - Try again and enter a number.\n")

                elif num.isdigit():
                    graph = Graph(int(num))
                    while True:
                        fifth_choice_menu()
                        option = input(" - Enter Your option: ")
                        print()
                        if option == "":
                            print(" - Try again and enter a valid option.\n")

                        elif option.lower() == "a":
                            graph.addVertex()

                        elif option.lower() == "b":
                            v1 = int(input(" - Enter the first vertex: "))
                            v2 = int(input(" - Enter the second vertex: "))
                            print()
                            graph.addEdge(v1, v2)

                        elif option.lower() == "c":
                            v = int(input(" - Enter the vertex to remove: "))
                            print()
                            graph.removeVertex(v)
                        
                        elif option.lower() == "d":
                            v1 = int(input(" - Enter the first vertex: "))
                            v2 = int(input(" - Enter the second vertex: "))
                            print()
                            graph.removeEdge(v1, v2)

                        elif option.lower() == "e":
                            degree = int(input(" - Enter the minimum degree to display: "))
                            graph.displayGraph(degree)

                        elif option.lower() == "f":
                            break

                        else:
                            print(" - Invalid Choice. Enter a valid option.")

            elif int(choice) == 6:
                break
                    


main()