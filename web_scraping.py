from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests    

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(START_URL)
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
soup = bs(page.text,'html.parser')

stars_data = []
stars_table = soup.find("table")
def scrape():
    table_rows = stars_table.find_all('tr')  
    for tr in table_rows :
        td = tr.find_all('td')
        row = [i.text.rstrip() for i in td]
        stars_data.append(row)

scrape()

stars_name = []
distance = []
mass = []
radius = []
luminousity = []

for i in range(1,len(stars_data)) :
    stars_name.append(stars_data[i][1])
    distance.append(stars_data[i][3])
    mass.append(stars_data[i][5])
    radius.append(stars_data[i][6])
    luminousity.append(stars_data[i][7])

df2 = pd.DataFrame(list(zip(stars_name,distance,mass,radius,luminousity)),columns = ['Stars_name','distance','mass','radius','luminousity'])
df2.to_csv('stars_data.csv')