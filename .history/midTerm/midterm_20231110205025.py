import json
import os
import requests
from bs4 import BeautifulSoup

open_tabs = []
def storeData():
    try:
        with open("", 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found")
        return None
file_path = 'C:\Users\User\foundations_cs_python\midTerm'


