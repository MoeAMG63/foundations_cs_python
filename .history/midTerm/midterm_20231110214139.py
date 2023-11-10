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

choice = int(input(""))

while True:
    if choice == 1:
        title = input("Enter a title to open a tab :")
        url = input("Enter url :")
        def handling_url_errors(url):
            try:
                result = requests.get(url)
                if result.status_code == 200:
                    return result.text
                else:
                    print("Error!")
                    return None
            except result.excep