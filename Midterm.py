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
        tab.append({"title": title, "url": parent_url, "content": doc.prettify()})
        return tab
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


def displayTabs():
    for i in range(len(tab)):
        print(f"the titles of tab {i + 1}:")
        print(tab[i]["title"].capitalize(), ":")
        if "nested tabs" in tab[i]:
            lst = tab[i]["nested tabs"]
            for i in lst:
                print(f"       - {i['title'].capitalize()}")
    return "These are the titles."


def nestedTabs(index):
    if index == "":
        print("Please enter a number to specify which tab you would like to add in.")
    if index < 1 and index > len(tab):
        print("Please try again and enter a valid number of a tab.")
    if index >= 1 and index <= len(tab):
        parent_tab = tab[index - 1]
        title = input(f"Enter the title of the nested tab of the website {tab[index - 1]['title'].capitalize()}: ")
        child_url = input(f"Enter the url of the nested tab of the website {tab[index - 1]['title'].capitalize()}: ")
        if validators.url(child_url):
            if child_url.startswith(parent_tab["url"]):
                if "nested tabs" not in parent_tab:
                    parent_tab["nested tabs"] = []

                parent_tab["nested tabs"].append({"title": title, "url": child_url})
            else:
                print("Your Url is not related to the website")
        else:
            print("Url is invalid, Please try again.")

    condition = input(
        "If you want to add another nested tab to this tab type YES, if not type NO: "
    ).lower()
    if condition == "yes":
        nestedTabs(index)
    elif condition == "no":
        return tab
    else:
        return tab

openTab()
nestedTabs(1)
displayTabs()