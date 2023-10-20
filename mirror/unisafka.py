from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import time
import pandas as pd


Options = webdriver.ChromeOptions()
Options.add_argument("headless")

#päivitä oma polku
Driver = webdriver.Chrome(options=Options, executable_path='/snap/bin/chromium.chromedriver')
Driver.get('https://unisafka.fi/tty')

time.sleep(3)

content = Driver.page_source
soup = BeautifulSoup(content, 'html.parser')

Hertsi = []  #1
Newton = []  #2
Konehuone = [] #3
Reaktor = [] #4

index = 0
#print(soup.prettify())
for s in soup.stripped_strings:
    
    if(s == "Hertsi"): index = 1
    if(s == "Newton"): index = 2
    if(s == 'Café Konehuone'): index = 3
    if(s == "Reaktori"): index = 4
    if(s == "/tty"): index = 0
    

    if(index == 1): Hertsi.append(s)
    if(index == 2): Newton.append(s)
    if(index == 3): Konehuone.append(s)
    if(index == 4): Reaktor.append(s)

Driver.quit()

# tee jotai järkevää noil listoil yms
print("hertsi")
print(Hertsi)
print("newton")
print(Newton)
print("konehuone")
print(Konehuone)
print("reaktori")
print(Reaktor)
    
def addRestaurant(restaurant):
    
    # check if restaurant is valid
    # restaurant must have name, timeOpen, vegan, lunch

    
    if len(restaurant) == 3:
        return False
    
    name = restaurant[0]
    timeOpen = restaurant[1]

    vegan = []
    lunch = []
    lunch2 = []

    tmp = []

    # index for data reading
    index = 0
    # find other parameters from list
    for i in restaurant[2::]:
        print(i)
        tmp.append(i)

        if "SOUP" in i or "keitto" in i:
            lunch2 = tmp
            tmp = []
        
        if "Lounas" in i or "LOUNAS I" in i or "FAVORITES" in i:
            lunch = tmp
            tmp = []
        
        if "LOUNAS II " in i:
            lunch2 = tmp
            tmp = []
        
        if "kasvis" in i or "KASVIS" in i or "VEGAN" in i:
            vegan = tmp
            tmp = []
    
    print("lunch")
    print(lunch)
    print("lunch2")
    print(lunch2)
    print("vegan")
    print(vegan)
    return

addRestaurant(Hertsi)
print()
addRestaurant(Newton)
print()
addRestaurant(Konehuone)
print()
addRestaurant(Reaktor)


