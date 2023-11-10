import json
import os
import requests
from bs4 import BeautifulSoup

open_tabs = []
def storeData():
    try:
        with open('JaCkSoN.json') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found")
        return None
file_path = 


