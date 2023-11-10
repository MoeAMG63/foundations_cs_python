import json
import os
import requests
from bs4 import BeautifulSoup

open_tabs = []
def storeData():
    
    with open('JaCkSoN.json') as file:
        data = json.load(file)
    

