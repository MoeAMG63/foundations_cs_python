import json
import os
import requests
from bs4 import BeautifulSoup

open_tabs = []
def storeData(open_tabs):
    with open('JaCkSoN.json') as file:
        data = json.load(file)
        new_string = json.dumps(data, indent=)
        print(data)

