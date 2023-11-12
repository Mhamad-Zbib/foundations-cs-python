import validators 
from bs4 import BeautifulSoup
import requests
import json
import os.path # To check the path of the file that the user should input exists

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
        tab.append({"title": title, "url": parent_url})
        return tab
    else:
        return "Url is invalid, Please try again."


def closeTab(index):
    if index == "":
        tab.pop()
        return tab
    elif index is not None:
        if index >= 1 and index <= len(tab):
            tab.pop(index - 1)
            return tab 
        else:
            return "Please enter a valid number of a tab."


def switchTab(index):
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
    if index >= 1 and index <= len(tab):
        parent_tab = tab[index - 1]
        title = input(
            f"Enter the title of the nested tab of the website {tab[index - 1]['title'].capitalize()}: ")
        child_url = input(
            f"Enter the url of the nested tab of the website {tab[index - 1]['title'].capitalize()}: ")

        if validators.url(child_url):
            if child_url.startswith(parent_tab["url"]):
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
        print( f"Please try again and enter Yes or No. \n This is Your tab with nested tabs now:\n   {tab}" )


def clearTabs():
    tab.clear()
    return f"Your tabs are clear. {tab}"


def saveTabs(file):
    if os.path.exists(file):
        with open(file, "w") as f:
            json.dump(tab, f, indent=4)
        return f"Tabs saved successfully to {file}."
    else:
        return "Please try again and enter a JSON file that exists." 
    

def importTabs(file):
    if os.path.exists(file):
        with open(file) as f:
            doc = json.load(f)
        return f"Tabs are successfully loaded from {file} \n {doc}"
    else:
        return "Please try again and enter a JSON file that exists."
    


def main():
    choice = 0
    while choice != 9:
        displayMenu()
        choice = int(input("Enter your choice: "))


        if choice == 1:
            print(openTab())
            print("--------")


        if choice == 2:
            index = input("Enter the number of which tab you want to close, OR press enter to remove the last tab: ")
            if index == "":
                closeTab(index)
            elif index.isdigit():
                if int(index) > 0:
                    closeTab(int(index))
                else:
                    print("Enter a number bigger than 0")
            else:
                print("Invalid input. Please enter a valid number!")
        

        if choice == 3:
            index = input("Enter the number of which tab you would like to display it's content: ")
            if index == "":
                print(switchTab(index))
            elif index.isdigit():
                if int(index) > 0 and int(index) <= len(tab):
                    print(switchTab(int(index)))
                else:
                    print("Invalid input. Please enter a valid number of a Tab! (bigger than 0)")
            else:
                print("Invalid input. Please enter a valid number of a Tab! (bigger than 0)")


        if choice == 4:
                print(displayTabs())
                print("---------")
        

main()