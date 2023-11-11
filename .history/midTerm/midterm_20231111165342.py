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
# def storeData():
#     file_path = 'C:\\Users\\User\\foundations_cs_python\\midTerm\\JaCkSoN.json'
#     try:
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         print("File not found")
#         return None
# json_path = storeData()
# open_tabs.append(json_path)
# print(open_tabs)

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
    open_tabs.clear()
    print("All Tabs are cleared.")
    print(open_tabs)


def CreateNestedTab(URl, Title, parent_indx ):

    nested_tab ={
        "Title" : Title,
        "URl" : URl
    }
    for tab in open_tabs:
        # if parent_indx == tab:
            if "Children" not in open_tabs:
                open_tabs[parent_indx]["Children"] = [nested_tab]
                return(open_tabs)
            else:
                open_tabs[parent_indx]["Children"].append(nested_tab)
                return (open_tabs)
    print("Nested Tab added Successfully.")


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
            
    elif choice == 4:
        displayTitle(open_tabs)
    elif choice == 6:
        clearAllTabs()
    elif choice == 5:
        parent_indx = int(input("Enter the index of the parent tab :"))
        Title = input("Enter your title :")
        URl = input("Enter the URL of the page you want to add : ")
        def handlingUrlErrors(URl):
            while True:
                if (URl.startswith("https://")) or (URl.startswith("http://")):
                    print(CreateNestedTab(URl, Title, parent_indx )
                    break
                else:
                    print("Error! Check! URL!")
                    URl = input("Enter the URL of the page you want to add : ")
        handlingUrlErrors(URl)
