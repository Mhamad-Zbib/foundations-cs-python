import validators # To check if the user's url is valid.
from bs4 import BeautifulSoup # To scrape information from web pages and to make the web page text from requests more readable.
import requests # To get the document behind the URL, and to feed that document to Beautifoul soup so .
import json # To save the current state of open tabs(data) in a json file.
import os.path  # To check the path of the file that the user should input exists.


print("------------")
name = input("Enter you name: ")
print("------------")
print(f"Welcome to the Browser Tabs Simulation {name.capitalize()}!")
print("------------")


def displayMenu(): # O(1).
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

# ----------------------------------------------------------------------------------------------------------------------

tab = []


def openTab(): # O(1).
    # Allowing the user to input website title and URL and then adding it to the global variable "tab".
    # And checking if the url inserted by the user is valid.
    title = input("Enter the title of the website: ")
    parent_url = input("Enter the url of the website: ")
    if validators.url(parent_url):
        tab.append({"title": title, "url": parent_url})
        return tab
    else:
        return "-------\nUrl is invalid, Please try again."

# ----------------------------------------------------------------------------------------------------------------------

def closeTab(index): # O(1).
    # This option gives the user a choice to close the last tab he opened or a tab he choosed it to close it.
    if index == "":
        print(
            f"Last tab with title {tab[-1]['title'].capitalize()} is removed, your tab now is:")
        tab.pop()
        return tab
    elif index is not None:
        if index >= 1 and index <= len(tab):
            print(
                f"Tab number {index} with title {tab[index - 1]['title'].capitalize()} is removed your tab now is: ")
            tab.pop(index - 1)
            return tab
        else:
            return "Please enter a valid number of a tab."

# ----------------------------------------------------------------------------------------------------------------------

def switchTab(index): # O(1).
    # This function permits the user to display the content(HTML code) of the last website or a any website he opened.
    lst = []
    if index == "":
        lst.append(tab[-1])
        result = requests.get(tab[0]["url"])
        doc = BeautifulSoup(result.text, "html.parser")
        return doc
    elif index >= 1 and index <= len(tab):
        lst.append(tab[index - 1])
        result = requests.get(tab[0]["url"])
        doc = BeautifulSoup(result.text, "html.parser")
        return doc
    else:
        return "Please try again and enter a valid number of a tab."

# ----------------------------------------------------------------------------------------------------------------------

def displayTabs(): # O(N^2), N being the length of the list.
    # Choosing this function by the user will display all the titles of all open tabs,
    #  and if there is any nested tabs it will display them hierarchically.
    for i in range(len(tab)):
        print(f"the titles of tab {i + 1}:")
        print(tab[i]["title"].capitalize(), ":")
        if "nested tabs" in tab[i]:
            lst = tab[i]["nested tabs"]
            for i in lst:
                print(f"       - {i['title'].capitalize()}")
    return "These are the titles."

# ----------------------------------------------------------------------------------------------------------------------

def nestedTabs(index): # O(N), N being the length of the list.
    # This option will permit the user to add as many nested tabs he wants to any tab he already opened. 
    if index >= 1 and index <= len(tab):
        parent_tab = tab[index - 1]
        title = input(
            f"Enter the title of the nested tab of the website {tab[index - 1]['title'].capitalize()}: ")
        child_url = input(
            f"Enter the url of the nested tab of the website {tab[index - 1]['title'].capitalize()}: ")

        if validators.url(child_url):
            if child_url.startswith(parent_tab["url"]):  # https://www.w3schools.com/python/ref_string_startswith.asp
                if "nested tabs" not in parent_tab:
                    parent_tab["nested tabs"] = []

                parent_tab["nested tabs"].append({"title": title, "url": child_url})
            else:
                print("Your Url is not related to the website")
        else:
            print("Url is invalid, Please try again.")

    print("------------")
    condition = input(
        "If you want to add another nested tab to this tab type YES, if not type NO: ").lower()

    if condition == "yes":
        print("------------")
        nestedTabs(index)
    elif condition == "no":
        print(f"Your tabs with nested tabs:\n {tab}")
    else:
        print(
            f"Please try again and enter Yes or No. \n This is Your tab with nested tabs now:\n   {tab}")

# ----------------------------------------------------------------------------------------------------------------------

def clearTabs(): # O(1).
    # This function will delete all opened tabs
    tab.clear()
    return f"Your tabs are clear.\n {tab}"

# ----------------------------------------------------------------------------------------------------------------------

def saveTabs(file): # O(1).
    # Here the function will save opened tabs in the user's JSON file path.
    if os.path.exists(file):
        with open(file, "w") as f:
            json.dump(tab, f, indent=4)
        return f"Tabs saved successfully to: {file}."
    else:
        return "Please try again and enter a JSON file that exists."

# ----------------------------------------------------------------------------------------------------------------------

def importTabs(file): # O(1)
    # After saving the opened tabs in the file path the user can load(display) the tabs from the file.
    if os.path.exists(file): # https://docs.python.org/3/library/os.path.html#module-os.path
        with open(file) as f:
            doc = json.load(f)
        return f"Tabs are successfully loaded from {file}: \n {doc}"
    else:
        return "Please try again and enter a JSON file that exists."

# ----------------------------------------------------------------------------------------------------------------------

def main(): # O(N^2), N being the length of the list , this is the worst case since the displayTabs function has the worst case between all functions O(N^2).
    choice = 0
    while choice != 9:
        displayMenu()
        choice = input("Enter your choice: ")


        if choice.isdigit():
            if int(choice) == 1:
                print(openTab())
                print("--------")



            if int(choice) == 2:
                if len(tab) == 0:
                    print("------------")
                    print(f"Your tab is already empty {tab}.")
                    print("------------")
                elif len(tab) != 0:
                    index = input(
                        "Enter the number of which tab you want to close, OR press enter to remove the last tab: ")
                    if index == "":
                        print(closeTab(index))
                    elif index.isdigit():
                        if int(index) > 0:
                            print(closeTab(int(index)))
                        else:
                            print("Enter a number bigger than 0")
                    else:
                        print("Invalid input. Please enter a valid number!")




            if int(choice) == 3:
                if len(tab) == 0:
                    print("------------")
                    print(f"Your tab is already empty {tab}. \nOpen a tab first using choice 1.")
                    print("------------")
                elif len(tab) != 0:
                    index = input(
                        "Enter the number of which tab you would like to display it's content: ")
                    if index == "":
                        print(switchTab(index))
                    elif index.isdigit():
                        if int(index) > 0 and int(index) <= len(tab):
                            print(switchTab(int(index)))
                        else:
                            print(
                                "Invalid input. Please enter a valid number of a Tab! (bigger than 0)")
                    else:
                        print(
                            "Invalid input. Please enter a valid number of a Tab! (bigger than 0)")





            if int(choice) == 4:
                if len(tab) == 0:
                    print("------------")
                    print(f"Your tab is already empty {tab}. \nOpen a tab first using choice 1.")
                    print("------------")
                elif len(tab) != 0:
                    print(displayTabs())
                    print("---------")




            if int(choice) == 5:
                if len(tab) == 0:
                    print("------------")
                    print(f"Your tab is already empty {tab}. \nOpen a tab first using choice 1.")
                    print("------------")
                elif len(tab) != 0:
                    index = input(
                        "Enter a number to specify which tab you would like to add nested tabs in: ")
                    if index.isdigit():
                        if int(index) < 1 or int(index) > len(tab):
                            print("Please try again and enter a valid number of a tab.")
                        elif int(index) >= 1 and int(index) <= len(tab):
                            nestedTabs(int(index))
                        else:
                            print("Please try again and enter a valid number of a tab.")
                    else:
                        print("Please try again and enter a valid number of a tab.")
                    print("------------")



            if int(choice) == 6:
                if len(tab) == 0:
                    print("------------")
                    print(f"Your tab is already empty {tab}.")
                    print("------------")
                elif len(tab) != 0:
                    print(clearTabs())
                    print("------------")



            if int(choice) == 7:
                if len(tab) == 0:
                    print("------------")
                    print(f"Your tab is already empty {tab} !\nOpen a tab first using choice 1.")
                    print("------------")
                elif len(tab) != 0:
                    file_path = input("Enter a file path in JSON format: ")
                    if file_path.startswith("C:"):
                        print("--------------")
                        print(saveTabs(file_path))
                        print("------------")
                    else:
                        print("------------")
                        print("Try again and enter a file path in JSON format")
                        print("------------")
                else:
                    print("Try again and enter a file path in JSON format")



            if int(choice) == 8:
                file = input("Enter a file path in JSON format: ")
                if file.startswith("C:"):
                    if os.path.getsize(file) == 0:
                        print("------------")
                        print(f"Your file is empty. \nPlease make sure to use choice 7 first.")
                        print("------------")
                    else:
                        print("------------")
                        print(importTabs(file))
                        print("------------")
                else:
                    print("------------")
                    print("Try again and enter a file path in JSON format")
                    print("------------")



            if int(choice) == 9:
                print("------------")
                print("Hope you enjoyed!")
                print("------------")
                break
            
            if int(choice) > 9:
                print("------------")
                print("Please try again and enter a number of which choice you would like to choose.")
                print("------------")

        else:
            print("------------")
            print("Please try again and enter a number of which choice you would like to choose.")
            print("------------")


main()
