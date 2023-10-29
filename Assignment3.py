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

    lst2 = []
    for row in range(num_col):
        print("------")
        print(f"For the second matrix enter elemets for the row number {row + 1}:")
        lst2.append([])
        for col in range(num_row):
            column = int(input(f"Enter element {col+ 1} of the row number {row + 1}: "))
            lst2[row].append(column)

    result = []
    for i in range(num_col):
        row = []
        for j in range(num_row):
            row.append(lst[j][i])
        result.append(row)
    if result == lst2:
        return True
    else:
        return False


def invertDict():
    num = int(input("Enter the number of keys: "))
    dictionary = {}
    dictionary2 = {}

    for i in range(num):
        key = input(f"Insert your key : ")
        value = input(f"Insert your value: ")
        dictionary.update({key: value})

    for key, value in dictionary.items():
        if value in dictionary2:
            dictionary2[value].append(key)
        else:
            dictionary2[value] = [key]
    return f"Before inverting: {dictionary} \n after inverting: {dictionary2}"


def convert():
    num = int(input("Enter the number of the IDs you want to insert: "))
    lst = []
    dictionary = {}

    for i in range(num):
        first_name = input(f"Enter name {i + 1}: ")
        last_name = input(f"Enter last name of {first_name.capitalize()}: ")
        id = input(
            f"Enter the ID of {first_name.capitalize()} {last_name.capitalize()}: "
        )
        job_title = input(
            f"Enter the job title of {first_name.capitalize()} {last_name.capitalize()}: "
        )
        company = input(
            f"Enter the company that {first_name.capitalize()} {last_name.capitalize()} work in : "
        )

        lstt = [first_name, last_name, id, job_title, company]
        lst.append(lstt)
        print("-------")

    for i in lst:
        dictionary[i[2]] = i[:2] + i[3:]
    return dictionary


def reverseWord(s):
    def isPalindrome(s):
        if s == "":
            return s
        return isPalindrome(s[1:]) + s[0]

    string = isPalindrome(s)
    if s == string:
        return f"{True}, Your string {s} is a Palindrome"
    else:
        return f"{False}, Your string {s} is not a Palindrome"


def mergeSort(l):
    if len(l) > 1:
        half = len(l) // 2
        left_half = l[:half]
        right_half = l[half:]
        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                l[k] = left_half[i]
                i += 1
            else:
                l[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            l[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            l[k] = right_half[j]
            j += 1
            k += 1
    return f"After Sorting: {l}"

def main():
    choice = 0
    while choice != 7:
        displayMenu()
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            addMatrices()
        if choice == 2:
            rotation()
        if choice == 3:
            invertDict()
        if choice == 4:
            convert()
        if choice == 5:
            string = input("Enter a word to check if it's a palindrome: ")
            if string.isalpha():
                reverseWord(string)
            

