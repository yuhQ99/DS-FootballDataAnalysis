from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

links = []
links_overview = []
players = []
list_countries = []
list_birthday = []
list_height = []
appearances = []
clean_sheets = []
wins = []
losses = []
saves = []
penalty_saves = []
punches = []
high_claimes = []
catches = []
sweeper_clearances = []
throws = []
goal_kicks = []
goal_concededs = []
error_lead_to_goals = []
own_goals = []
yellow_cards = []
red_cards = []
fouls = []
goals = []
assists = []
total_passes = []
total_pass_per_games = []
long_balls = []

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver_linux64/chromedriver',options=options)


#get link of player 2019/20
driver.get("https://www.premierleague.com/players?se=274&cl=-1")

# Get scroll height after first time page load
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(2)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

content = driver.page_source
soup = BeautifulSoup(content, features="lxml")

for a in soup.findAll('a', class_ = 'playerName'):
    td = a.findNext('td')
    if(td.text == 'Goalkeeper'):
        link = a['href']
        link = link.replace("//", "https://")
        links_overview.append(link)
        link = link.replace("overview", "stats?co=1&se=274")
        links.append(link)

for link in links_overview:
    driver.get(link)
    print("Get Personal Information of " + link)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    div = soup.find('div', class_='personalLists')
    if(div!=None):
        country = div.find('span', class_='playerCountry')
        if (country == None):
            list_countries.append(country)
        else:
            list_countries.append(country.text)
            print(country.text)
        label = div.find('div', text='Date of Birth')
        if (label == None):
            list_birthday.append(label)
        else:
            birth = label.findNext('div', class_='info')
            birth = birth.text.strip()
            if (len(birth) > 10):
                birth = birth.split(' ')[0]
            list_birthday.append(birth)
            print(birth)
        label = div.find('div', text='Height')
        if (label == None):
            list_height.append(label)
            print(label)
        else:
            height = label.findNext('div', class_='info')
            h = height.text.replace("cm", "")
            list_height.append(h)
            print(h)
    else:
        list_countries.append("")
        list_birthday.append("")
        list_height.append("")

for link in links:
    driver.get(link)
    time.sleep(5)

    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")

    name = soup.find('div', 'name t-colour')
    players.append(name.text)

    appearance = soup.find('span', 'allStatContainer statappearances')
    appearances.append(appearance.text)

    cs = soup.find('span', 'allStatContainer statclean_sheet')
    clean_sheets.append(cs.text)

    win = soup.find('span', 'allStatContainer statwins')
    wins.append(win.text)

    loss = soup.find('span', 'allStatContainer statlosses')
    losses.append(loss.text)

    save = soup.find('span', 'allStatContainer statsaves')
    saves.append(save.text)

    penalty_save = soup.find('span', 'allStatContainer statpenalty_save')
    penalty_saves.append(penalty_save.text)

    punch = soup.find('span', 'allStatContainer statpunches')
    punches.append(punch.text)

    high_claim = soup.find('span', 'allStatContainer statgood_high_claim')
    high_claimes.append(high_claim.text)

    catch = soup.find('span', 'allStatContainer statcatches')
    catches.append(catch.text)

    sweeper_clearance = soup.find('span', 'allStatContainer stattotal_keeper_sweeper')
    sweeper_clearances.append(sweeper_clearance.text)

    throw = soup.find('span', 'allStatContainer statkeeper_throws')
    throws.append(throw.text)

    goal_kick = soup.find('span', 'allStatContainer statgoal_kicks')
    goal_kicks.append(goal_kick.text)

    goal_conceded = soup.find('span', 'allStatContainer statgoals_conceded')
    goal_concededs.append(goal_conceded.text)

    error_lead_to_goal = soup.find('span', 'allStatContainer staterror_lead_to_goal')
    error_lead_to_goals.append(error_lead_to_goal.text)

    own_goal = soup.find('span', 'allStatContainer statown_goals')
    own_goals.append(own_goal.text)

    yellow_card = soup.find('span', 'allStatContainer statyellow_card')
    yellow_cards.append(yellow_card.text)

    red_card = soup.find('span', 'allStatContainer statred_card')
    red_cards.append(red_card.text)

    foul = soup.find('span', 'allStatContainer statfouls')
    fouls.append(foul.text)

    goal = soup.find('span', 'allStatContainer statgoals')
    goals.append(goal.text)

    assist = soup.find('span', 'allStatContainer statgoal_assist')
    assists.append(assist.text)

    total_pass = soup.find('span', 'allStatContainer stattotal_pass')
    total_passes.append(total_pass.text)

    total_pass_per_game = soup.find('span', 'allStatContainer stattotal_pass_per_game')
    total_pass_per_games.append(total_pass_per_game.text)

    long_ball = soup.find('span', 'allStatContainer stataccurate_long_balls')
    long_balls.append(long_ball.text)

df = pd.DataFrame({'Name': players,
                   'Country': list_countries,
                   'Date of Birth': list_birthday,
                   'Height': list_height,
                   'Appearance': appearances,
                   'Wins': wins,
                   'Losses': losses,
                   'Clean Sheet': clean_sheets,
                   'Saves': saves,
                   'Penalty Save': penalty_saves,
                   'Punch': punches,
                   'High Claim': high_claimes,
                   'Catch': catches,
                   'Sweeper Clearance': sweeper_clearances,
                   'Throw': throws,
                   'Goal Kick': goal_kicks,
                   'Goal Conceded': goal_concededs,
                   'Error Lead To Goal': error_lead_to_goals,
                   'Own Goal': own_goals,
                   'Yellow Card': yellow_cards,
                   'Red Card': red_cards,
                   'Foul': fouls,
                   'Goal': goals,
                   'Assist': assists,
                   'Total Pass': total_passes,
                   'Total Pass Per Game': total_pass_per_games,
                   'Long Ball': long_balls})

df.to_csv('../data/goalkeepers.csv', index=False, encoding='utf-8')


