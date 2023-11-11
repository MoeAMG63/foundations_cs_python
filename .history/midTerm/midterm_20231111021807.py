import json
import os
import requests
from bs4 import BeautifulSoup

open_tabs = []
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
open_tabs.append(json_path)
print(open_tabs)

def OpenTab(Title, URl):
    NewTab = {
        "Title" : Title,
        "URl": URl
    }
    open_tabs.append(NewTab)
    print(open_tabs)


def distitle(open_tabs):
    for tab in open_tabs:
        print
        






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
    elif choice == 2:
        index = int(input("Enter the index of the tab you wanna close :"))
    CloseTab(index)
