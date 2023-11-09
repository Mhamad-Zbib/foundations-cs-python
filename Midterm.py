print("------------")
name = input("Enter you name: ")
print(f"Welcome to the Browser Tabs Simulation {name.capitalize()}!")


def displayMenu():
    # The menu is here to display what options the user can pick.
    print(
        "The menu:\n"
        "     1. Open Tab \n"
        "     2. Close Tab \n"
        "     3. Switch Tab \n"
        "     4. Display All Tabs \n"
        "     5. Open Nested Tab \n"
        "     6. Clear All Tabs \n"
        "     7. Save Tabs \n"
        "     8. Import Tabs \n"
        "     9. Exit"
    )


tab = []


def openTab():
    title = input("Enter the title of the website: ")
    url = input("Enter the url of the website: ")
    tab.append({"title": title, "url": url, "content": ""})


def closeTab(index):
    if index == "":
        tab.pop()
    elif index is not None:
        if index >= 1 and index <= len(tab):
            tab.pop(index - 1)
        else:
            print("Please enter a valid number of a tab.")
