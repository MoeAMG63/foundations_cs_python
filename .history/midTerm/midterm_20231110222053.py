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
        "URL": URl
    }
    open_tabs.append(NewTab)
    print(open_tabs)
    
choice = int(input(""))
while True:
    if choice == 1:
        Title = input("Enter a title to open a tab :")
        URl = input("Enter url :")
        def handlingUrlErrors(URl):
            if not (URl.startswith("https://")) or (URl.startswith("http://")):
                print("Error! Enter you URL starting with (https://) or ")
        OpenTab(Title, URl)

