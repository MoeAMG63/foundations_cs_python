import json
import os
import requests
from bs4 import BeautifulSoup

open_tabs = [
            {
                "Title" : "w3schools",
                "URl" : "https://www.w3schools.com/"
            },
            {
                "Title" : "Google",
                "URl" : "https://www.google.com/",
                "Children" : [
                    {
                        "Title" : "Youtube",
                        "URl" : "https://www.youtube.com/"
                    },
                    {
                        "Title" :"Google Drive",
                        "URl" : "https://www.googledrive.com/"
                    }
                ]
            },
            {
                "Title" : "Coding Game",
                "URl" : "https://www.codingame.com/"
            },
            {
                "Title" : "SE Factory",
                "URl" : "https://www.sefactory.io/"
            }
            ]

imported_data = []
def SaveTabs(file_path, openTabs):
    try:
        with open(file_path, 'w') as file:
            json.dump(open_tabs, file, indent=2)
    except FileNotFoundError:
        print("File doesn't exist")
        return None

def OpenTab(Title, URl):
    NewTab = {
        "Title" : Title,
        "URL": URl
    }
    open_tabs.append(NewTab)
    print(open_tabs)
    
def displayTitle(open_Tabs):
    for tab in open_Tabs:
        print(tab['Title'])
        if 0 < len(tab) > 2:
            for nest in tab["Children"]:
                print(" =>: "  ,nest["Title"]) 

def clearAllTabs():
    print("Tabs Before Deletion :")
    print(open_tabs)
    open_tabs.clear()
    print("All Tabs are cleared.")
    print(open_tabs)


def CreateNestedTab(URl, Title, parent_indx):

    nested_tab ={
        "Title" : Title,
        "URl" : URl
    }
    if "Children" not in open_tabs:
        open_tabs[parent_indx]["Children"] = [nested_tab]
        
        return(open_tabs)
    else:
        open_tabs[parent_indx]["Children"].append(nested_tab)
        return (open_tabs)

def CloseTab(index1=None):
    if index1 is None:
        if open_tabs:
            tab_to_close = open_tabs.pop()
            print(f"Closed Tab => : {tab_to_close}")
            print(open_tabs)
        else:
            print("No Tabs")
    tab_found = False
    for i in range(len(open_tabs)):
        if index1 == i:
            tab_to_remove = open_tabs[i]
            open_tabs.remove(tab_to_remove)
            tab_found = True
            print(open_tabs)
    if not tab_found:
        print("No Tab Found at this Index!")




def loadTabs(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found")
        return None





choice = int(input("Choose from the menu :"))
while True:
    if choice == 1:
        Title = input("Enter a title to open a tab :")
        URl = input("Enter the URL of the page you want to open : ")
        def handlingUrlErrors(URl):
            while True:
                if (URl.startswith("https://")) or (URl.startswith("http://")):
                    OpenTab(URl, Title)
                    break
                else:
                    print("Error! Check! URL!")
                    URl = input("Enter the URL of the page you want to open : ")
        handlingUrlErrors(URl)
    elif choice == 2:
        index1 = input("Enter the number of the Tab you want to close (or press Enter to close the last tab): ")
        if index1.isdigit():
            open_tabs.remove(open_tabs[int(index1)])
            print("Deleted tab => : ", open_tabs[int(index1)])
        else:
            open_tabs.remove(open_tabs[])

    elif choice == 3:
        pass
    elif choice == 4:
        displayTitle(open_tabs)
        break
    elif choice == 5:
        parent_indx = int(input("Enter the index of the parent tab :"))
        Title = input("Enter your title :")
        URl = input("Enter the URL of the page you want to add : ")
        def handlingUrlErrors(URl):
            while True:
                if (URl.startswith("https://")) or (URl.startswith("http://")):
                    print(CreateNestedTab(URl, Title, parent_indx ))
                    print("Nested Tab added Successfully.")
                    break
                else:
                    print("Error! Check! URL!")
                    URl = input("Enter the URL of the page you want to add : ")
        handlingUrlErrors(URl)
    elif choice == 6:
        clearAllTabs()
        break
    elif choice == 7:
        file_path = input("Enter your file path :")
        json_path = SaveTabs(file_path, open_tabs)
        open_tabs.append(json_path)
        print(open_tabs)

    elif choice == 8:
        file_path = input("Enter a file path :")
        json_path = loadTabs(file_path)
        imported_data.append(json_path)
        print(imported_data)
    elif choice == 9:
        break