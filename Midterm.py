import validators
from bs4 import BeautifulSoup
import requests

print("------------")
name = input("Enter you name: ")
print("------------")
print(f"Welcome to the Browser Tabs Simulation {name.capitalize()}!")
print("------------")


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
    parent_url = input("Enter the url of the website: ")
    if validators.url(parent_url):
        result = requests.get(parent_url)
        doc = BeautifulSoup(result.text, "html.parser")
        tab.append(
            {"title": title, "url": parent_url, "content": doc.prettify()}
        )
    else:
        print("Url is invalid, Please try again.")


def closeTab(index):
    if index == "":
        tab.pop()
    elif index is not None:
        if index >= 1 and index <= len(tab):
            tab.pop(index - 1)
        else:
            print("Please enter a valid number of a tab.")


def switchTab(index):
    lst = []
    if index == "":
        lst.append(tab[-1])
        return lst[0]["content"]
    elif index is not None:
        if index >= 1 and index <= len(tab):
            lst.append(tab[index - 1])
            return lst[0]["content"]


def nestedTabs(index):
    if index == "":
        print("Please enter a number to specify which tab you would like to add in.")
    if index < 1 and index > len(tab):
        print("Please try again and enter a valid number of a tab.")
    if index >= 1 and index <=len(tab):
        parent_tab = tab[index - 1]
        title = input("Enter the title of the nested tab of the website: ")
        child_url = input("Enter the url of the nested tab of the website: ")
        if validators.url(child_url):
            if child_url.startswith(parent_tab["url"]):
                if "nested tabs" not in parent_tab:
                    parent_tab["nested tabs"] = []

                parent_tab["nested tabs"].append({"title": title, "url": child_url})
            else:
                print("Your Url is not related to the website")
        else:
            print("Url is invalid, Please try again.")
    return tab


    