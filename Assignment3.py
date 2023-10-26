def displayMenu():
    name = input("Enter your name: ")
    print("Welcome", name)
    print(
        "1. Add Matrices\n"
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