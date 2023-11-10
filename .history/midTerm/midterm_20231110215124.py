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

def OpenTab(Title, Url):
    NewTab = {
        
    }

while True:
    if choice == 1:
        title = input("Enter a title to open a tab :")
        url = input("Enter url :")
        def handlingUrlErrors(url):
            try:
                result = requests.get(url)
                if result.status_code == 200:
                    return result.text
                else:
                    print("Error!")
                    return None
            except requests.exceptions.MissingSchema:
                print("Error! : Check your URL carefully")
                return None
            except requests.exceptions.RequestException:
                print("ERROR!!")
                return None
        process = handlingUrlErrors(url)
        if process is not None:
            print(process)
        else:
            print("Check the URL carfully")

