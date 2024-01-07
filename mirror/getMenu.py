import requests
from datetime import datetime
import json

"""
Fetch the menu data from the API 
url = unisafka.fi
Parse data into python object and store it in a list.
Object contains restaurant name, open today, eating hours and menu.
Only tty restaurants are needed.
Sundays are not needed. ( not open )

"""

week_days = ['su','ma', 'ti', 'ke', 'to', 'pe', 'la']


def get_date():
    #get todays date, 
    # return list containing info
    # year;week;weeK-day
    ## TESTATTU

    date = datetime.now().strftime("%Y;%W;%w").split(";")
    date[2] = week_days[int(date[2])]
    return date

def get_version(date: list):
    #version needs to get by api
    #it needs year and week
    # return string version number

    url = f"https://unisafka.fi/static/json/{date[0]}/{date[1]}/v.json"
    #print("url: " + url)
    response = requests.get(url)
    print("response code (get_version): " + str(response.status_code))
    return response.json().get("v")

def get_url(date: list, version: str):
    #formalize url address and return it as string

    return f"https://unisafka.fi/static/json/{date[0]}/{date[1]}/{version}/{date[2]}.json"



def fetchData(url):
    # fetch api data and load it to python object
    # return python object

    response = requests.get(url)
    print("response code (fetchData): " + str(response.status_code))

    text = json.loads(response.text)
    return text


# Create Restaurant objects from the data and store them in a list

def get_restaurants(data):
    # get tty restaurants data in a list

    tty_res = data.get("restaurants_tty")
    # get tty restaurants in a list
    res_data = [tty_res.get("res_hertsi"),tty_res.get("res_newton"),tty_res.get("res_konehuone"),tty_res.get("res_reaktori")]

    return [Restaurant(res_data) for res_data in res_data]

class Restaurant:
    def __init__(self, data):
        self.name = data['restaurant']
        self.open_today = data['open_today']
        self.eating_hours = data['eating_hours']
        self.menu = []

        # Extract the meal data from 'meals' and 'meals_en' and store it in the menu
        for meal_data in data['meals']:
            meal_name = meal_data['kok']
            meal_items = [item['mpn'] for item in meal_data['mo']]
            self.menu.append([meal_name, meal_items])

    def __str__(self):
        return f"Restaurant: {self.name}\nOpen today: {self.open_today}\nEating hours: {self.eating_hours}\nMenu: {self.menu}"
    
"""
date = get_date()
version = get_version(date)

#print("date: " + str(date))
#print("version: " + str(version))

url = get_url(date, version)
print("url: " + url)

dataDict = fetchData(url)

print(dataDict.get("restaurants_tty").keys())
restaurants = get_restaurants(dataDict)
# Print the details of each restaurant
"""


