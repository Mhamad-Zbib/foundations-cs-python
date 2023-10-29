def displayMenu():
    name = input("Enter your name: ")
    print("Welcome", name)
    print(
        "  1. Add Matrices\n"
        + "2. Check Rotation\n"
        + "3. Invert Dictionary\n"
        + "4. Convert Matrix to Dictionary\n"
        + "5. Check Palindrome\n"
        + "6. Search for an Element & Merge Sort\n"
        + "7.Exit"
    )


def addMatrices():
    num_row = int(input("Enter number of rows: "))
    num_col = int(input("Enter number of columns: "))
    lst = []

    for row in range(num_row):
        print("------")
        print(f"For the first matrix enter elemets for the row number {row + 1}:")
        lst.append([])
        for col in range(num_col):
            column = int(input(f"Enter element {col+ 1} of the row number {row + 1}: "))
            lst[row].append(column)

    lst2 = []
    for row in range(num_row):
        print("------")
        print(f"For the second matrix enter elemets for the row number {row + 1}:")
        lst2.append([])
        for col in range(num_col):
            column = int(input(f"Enter element {col+ 1} of the row number {row + 1}: "))
            lst2[row].append(column)

    result = []
    for i in range(num_row):
        row = []
        for j in range(num_col):
            row.append(lst[i][j] + lst2[i][j])
        result.append(row)
    return f"The resulting sum of the matrices is: {result}"


def rotation():
    num_row = int(input("Enter number of rows: "))
    num_col = int(input("Enter number of columns: "))
    lst = []

    for row in range(num_row):
        print("------")
        print(f"For the first matrix enter elemets for the row number {row + 1}:")
        lst.append([])
        for col in range(num_col):
            column = int(input(f"Enter element {col+ 1} of the row number {row + 1}: "))
            lst[row].append(column)
