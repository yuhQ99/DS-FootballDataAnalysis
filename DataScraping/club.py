from bs4 import BeautifulSoup
import requests
import pandas as pd
# import constant
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import csv


Options = webdriver.ChromeOptions()
Options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path='/usr/local/bin/chromedriver.exe', chrome_options=Options)

attribute_dict = dict()
data = dict()
# retrieved data
dataList = dict()
# retrieved data
teamList = dict()
final = dict()
final_arr = dict()
teams = ['Leicester City', 'Southampton', 'Wolverhampton Wanderers', 'Liverpool', 'Arsenal', 'Tottenham Hotspur', 'Watford', 'AFC Bournemouth', 'Manchester United', 'Everton',
         'Aston Villa', 'Norwich City', 'Burnley', 'Newcastle United', 'Crystal Palace', 'West Ham United', 'Sheffield United', 'Chelsea', 'Manchester City', 'Brighton and Hove Albion']

for i in teams:
    final[i] = dict()
    final_arr[i] = []


# get all attributes
attribute_url = 'https://www.premierleague.com/stats/top/clubs/losses?se=274'
page = requests.get(attribute_url)
mySoup = BeautifulSoup(page.content, 'html.parser')
attribute = mySoup.body.find_all(attrs={"role": "option"})

for i in range(len(attribute)):
    attribute_dict[attribute[i].text.strip()] = attribute[i].text.strip()

attribute_display = attribute_dict

attribute_dict['Own goals'] = "own_goals"
attribute_dict['Yellow cards'] = "total_yel_card"
attribute_dict['Red cards'] = "total_red_card"
attribute_dict['Passes'] = "total_pass"
attribute_dict['Shots'] = "total_scoring_att"
attribute_dict['Offsides'] = "total_offside"
attribute_dict['Hit woodwork'] = 'hit_woodwork'
attribute_dict['Big chances missed'] = 'big_chance_missed'
attribute_dict['Tackles'] = 'total_tackle'
attribute_dict['Clearances'] = 'total_clearance'
attribute_dict['Clearances off line'] = 'clearance_off_line'
attribute_dict['Dispossessed'] = 'dispossessed'
attribute_dict['Clean sheets'] = 'clean_sheet'
attribute_dict['Penalties Saved'] = 'penalty_save'
attribute_dict['High claims'] = 'total_high_claim'
# attribute_dict['punches'] = 'punches'

print(attribute_dict)
# test variables
test = ['Own goals']
for i in attribute_dict:
    for j in teams:
        final[j][i] = 0
# scraping
for att in attribute_dict:
    # here is the url we're gonna scraping
    scrape_url = 'https://www.premierleague.com/stats/top/clubs/' + \
        attribute_dict[att] + '?se=274'

    # html_page
    # page = requests.get(scrape_url)
    driver.get(scrape_url)
    time.sleep(4)
    # print(page.status_code)
    # parse html_page into BeautifulSoup
    # mySoup = BeautifulSoup(page.content, 'html.parser')
    content = driver.page_source
    mySoup = BeautifulSoup(content, 'html.parser')
    # print(mySoup)
    data = mySoup.find_all("td", class_="mainStat text-centre")
    # print(data)
    # list data of that attribute
    dataList[att] = []
    teamList[att] = []

    team = mySoup.find_all("a", class_="playerName")
    # print(i)
    # print(len(data))
    for dt in range(len(data)):
        dataTemp = data[dt].text
        dataList[att].append(dataTemp)
        teamTemp = team[dt].text.strip()
        teamList[att].append(teamTemp)
 
        final[teamTemp][att] = dataTemp
        final_arr[teamTemp].append(dataTemp)
        
    # print(teamList[att])

# print(final)
# first character of team name should be in upper-case
# print(final['Liverpool'])
# csv_columns = dict()

# for i in attribute_dict:
#     csv_columns[i] = 'i'

# csv_file = "Clubs.csv"
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         for team in teams:
#             writer.writerow(final[team])
# except IOError:
#     print("I/O error")

# for team in teams:
#     df = pd.DataFrame(final_arr[team])

