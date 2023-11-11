import json
import os
import requests
from bs4 import BeautifulSoup

open_Tabs = []
def storeData():
    file_path = 'C:\\Users\\User\\foundations_cs_python\\midTerm\\JaCkSoN.json'
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found")
        return None
json_path = storeData()
open_Tabs.append(json_path)
print(open_Tabs)

def OpenTab(Title, URl):
    NewTab = {
        "Title" : Title,
        "URl": URl
    }
    open_Tabs.append(NewTab)
    print(open_Tabs)


def displayTitle(open_Tabs):
    for tab in open_Tabs[0]["tabs"]:
        print(tab['Title'])
        if len(tab) > 2:
            for nest in tab["Children"]:
                print(" =>: "  ,nest["Title"])
        


def clearAllTabs():
    open_Tabs.clear()
    print("All Tabs are cleared.")
    print(open_Tabs)


def CreateNestedTab(parent_indx, URl, Title):
    nested_tab ={
        "Title" : Title,
        "URl" : URl
    }
    for tab in open_Tabs[0]["tabs"]:
        if 0 < len(tab) > 2:
            parent = tab["Children"]
            parent.app
    



storeData()
choice = int(input("Choose from the menu :"))

while True:
    if choice == 1:
        Title = input("Enter a title to open a tab :")
        URl = input("Enter url :")
        def handlingUrlErrors(URl):
            if not (URl.startswith("https://")) or (URl.startswith("http://")):
                print("Error! Enter you URL starting with (https://) or (http://)")
                return None
            result = handlingUrlErrors(URl)
            if result is not None:
                print(result)
            else:
                print("URL! CHECK!")
        OpenTab(Title, URl)
    # elif choice == 2:
    #     index = int(input("Enter the index of the tab you wanna close :"))
    # CloseTab(index)
    elif choice == 4:
        displayTitle(open_Tabs)
    elif choice == 6:
        clearAllTabs()
    break