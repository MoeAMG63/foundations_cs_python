import json
import os
import requests
from bs4 import BeautifulSoup

open_tabs = []
def storeData(new_string):
    with open('JaCkSoN.json') as file:
        data = json.load(file)
        new_string = json.dumps(data, indent=2)
        print(data)

