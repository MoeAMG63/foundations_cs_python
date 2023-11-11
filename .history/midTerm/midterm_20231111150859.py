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
    
choice = int(input("Choose from the menu :"))
while True:
    if choice == 1:
        Title = input("Enter a title to open a tab :")
        URl = input("Enter url :")
        def handlingUrlErrors(URl):
            while True:
                if (URl.startswith("https://")) or (URl.startswith("http://")):
                    CreateNestedTab(URl, Title)
                    break
                else:
                    print("Error! Check! URL!")
                    URl = input("Enter the URL of the page you want to add a nested Tab to : ")
                OpenTab(Title, URl)
    elif choice == 2:
        pass