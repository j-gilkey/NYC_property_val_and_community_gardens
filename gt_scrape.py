import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_garden_list():

    page = requests.get("https://greenthumb.nycgovparks.org/gardensearch.php#garden-list")

    manhattan_list = soup.find("div", {"id": "tabs-m"})
    #just getting manhattan to start, the 'm' in the idea name indicates manhattan_list

    man_garden_list = manhattan_list.find_all(class_="garden-row")
    #now get the garden elements

    all_gardens = []
    for item in man_garden_list:
        garden_list = item.find_all(text=True)
        #get all text

        garden_list = [str(i.strip()) for i in garden_list]
        #remove whitespace

        garden_1 = {'name': garden_list[2], 'address': garden_list[3]}
        all_gardens.append(garden_1)
        #grab the first garden and append it

        if len(garden_list) == 15:
             garden_2 = {'name': garden_list[9], 'address': garden_list[10]}
             all_gardens.append(garden_2)
             #confirm the second garden exists and then append that one too
    return all_gardens

print(scrape_garden_list())
