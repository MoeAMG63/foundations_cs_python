import json
import os
from bs4 import BeautifulSoup
import requests

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


import_data = []
def SaveTabs(file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(open_tabs, file, indent=2)
            print("Data is Saved!")
        return file
    except FileNotFoundError:
        print("File not found")
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

def CloseTab(index_of_tab, open_tabs):
    if not index_of_tab:
        deletedTab = open_tabs.pop(-1)
        print(f"Last tab deleted => : {deletedTab}")
        return
    try:
        index = int(index_of_tab)
        if index >= 0 and index < (len(open_tabs)):
            deleted_tab = open_tabs.pop(index)
            print(f"Deleted Tab => : {deleted_tab}")
        else:
            print("Index out of range.")
    except ValueError as ve:
        print(f"Value Error : {ve}")
        print("Enter an integer!!!")



def loadTabs(file_path2):
    try:
        with open(file_path2, 'r') as file2:
            data = json.load(file2)
        return data
    except FileNotFoundError as fn:
        print(f"File not found : {fn}")
        return None
    except PermissionError as pe:
        print(f"Permission error! {pe}")
    except ValueError as ve:
        print(f"Enter a File Path! {ve}")

def webScrap(tab_index):
    try:
        if tab_index:
            tab = open_tabs[tab_index]
            scrape_url = tab["URl"]
            html_content = requests.get(scrape_url)
            if html_content.status_code == 200:
                content = BeautifulSoup(html_content.text, 'html.parser')
                print(content.findAll())
            else:
                print("Failed to scrape")
        else:
            tab = open_tabs[-1]
            scrape_url = tab["URl"]
            html_content = requests.get(scrape_url)
            if html_content.status_code == 200:
                content = BeautifulSoup(html_content.text, 'html.parser')
                print(content.findAll())
    except IndexError:
        print("Invalid Tab index!")
    except ValueError:
        print("Enter an integer!")


menu = '''
1.Open Tab
2.Close Tab
3.Switch Tab
4.Display All Tabs
5.Open Nested Tabs
6.Clear All Tabs
7.Save Tabs
8.Import Tabs
9.Exit
'''
print(menu)
print("-" * 50)
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
        index_of_tab = input("Enter the number of the Tab you want to close (or press Enter to close the last tab): ")
        CloseTab(index_of_tab, open_tabs)
        
    elif choice == 3:
        tab_index =int(input("Enter the tab index to web scrape it :"))
        webScrap(tab_index)
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
        SaveTabs(file_path)
    elif choice == 8:
        file_path2 = input("Enter a file path :")
        json_path = loadTabs(file_path2)
        import_data.append(json_path)
        print("Loaded Tabs :")
        print(import_data)
    elif choice == 9:
        pass
