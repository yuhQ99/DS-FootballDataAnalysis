import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

links = []
links_overview = []
list_players = []
list_countries = []
list_birthday = []
list_height = []
list_appearances = []
list_goals = []
list_wins = []
list_losses = []
list_goals_per_game = []
list_head_goals = []
list_goals_with_right_foot = []
list_goals_with_left_foot = []
list_penalties_scored = []
list_free_kicks_scored = []
list_shots = []
list_shots_on_target = []
list_shot_accuracy_rates = []
list_hit_woodwork = []
list_big_chances_missed = []
list_assists = []
list_total_passes = []
list_total_passes_per_game = []
list_big_chances_created = []
list_crosses = []
list_yellow_cards = []
list_red_cards = []
list_fouls = []
list_offside = []
list_tackles = []
list_blocked_shot = []
list_interceptions = []
list_clearances = []
list_headed_clearances = []

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver_linux64/chromedriver', options=options)

# get link of player 2019/20
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

for a in soup.findAll('a', class_='playerName'):
    td = a.findNext('td')
    if (td.text == 'Forward'):
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

    country = div.find('span', class_='playerCountry')
    if(country==None):
        list_countries.append(country)
    else:
        list_countries.append(country.text)
        print(country.text)
    label = div.find('div', text='Date of Birth')
    birth = label.findNext('div', class_='info')
    if(birth==None):
        list_birthday.append(birth)
    else:
        birth = birth.text.strip()
        if(len(birth)>10):
            birth = birth.split(' ')[0]
        list_birthday.append(birth)
        print(birth)
    label = div.find('div', text='Height')
    if(label==None):
        list_height.append(label)
        print(label)
    else:
        height = label.findNext('div', class_='info')
        h = height.text.replace("cm", "")
        list_height.append(h)
        print(h)
for link in links:
    driver.get(link)
    time.sleep(5)
    print(link)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")

    name = soup.find('div', 'name t-colour')
    if (name == None):
        list_players.append(name)
    else:
        list_players.append(name.text)

    appearance = soup.find('span', 'allStatContainer statappearances')
    if (appearance == None):
        list_appearances.append(appearance)
    else:
        list_appearances.append(appearance.text)

    goal = soup.find('span', 'allStatContainer statgoals')
    if (goal == None):
        list_goals.append(goal)
    else:
        list_goals.append(goal.text)

    win = soup.find('span', 'allStatContainer statwins')
    if (win == None):
        list_wins.append(win)
    else:
        list_wins.append(win.text)

    loss = soup.find('span', 'allStatContainer statlosses')
    if (loss == None):
        list_losses.append(loss)
    else:
        list_losses.append(loss.text)

    goals_per_game = soup.find('span', class_='allStatContainer statgoals_per_game')
    if (goals_per_game == None):
        list_goals_per_game.append(goals_per_game)
    else:
        list_goals_per_game.append(goals_per_game.text)

    headed_goal = soup.find('span', 'allStatContainer statatt_hd_goal')
    if (headed_goal == None):
        list_head_goals.append(headed_goal)
    else:
        list_head_goals.append(headed_goal.text)

    goals_with_right_foot = soup.find('span', 'allStatContainer statatt_rf_goal')
    if (goals_with_right_foot == None):
        list_goals_with_right_foot.append(goals_with_right_foot)
    else:
        list_goals_with_right_foot.append(goals_with_right_foot.text)

    goals_with_left_foot = soup.find('span', 'allStatContainer statatt_lf_goal')
    if (goals_with_left_foot == None):
        list_goals_with_left_foot.append(goals_with_left_foot)
    else:
        list_goals_with_left_foot.append(goals_with_left_foot.text)

    penalties_scored = soup.find('span', 'allStatContainer statatt_pen_goal')
    if (penalties_scored == None):
        list_penalties_scored.append(penalties_scored)
    else:
        list_penalties_scored.append(penalties_scored.text)

    free_kicks_scored = soup.find('span', 'allStatContainer statatt_freekick_goal')
    if (free_kicks_scored == None):
        list_free_kicks_scored.append(free_kicks_scored)
    else:
        list_free_kicks_scored.append(free_kicks_scored.text)

    shots = soup.find('span', 'allStatContainer stattotal_scoring_att')
    if (shots == None):
        list_shots.append(shots)
    else:
        list_shots.append(shots.text)

    shots_on_target = soup.find('span', 'allStatContainer statontarget_scoring_att')
    if (shots_on_target == None):
        list_shots_on_target.append(shots_on_target)
    else:
        list_shots_on_target.append(shots_on_target.text)

    shot_accuracy_rate = soup.find('span', 'allStatContainer statshot_accuracy')
    if (shot_accuracy_rate == None):
        list_shot_accuracy_rates.append(shot_accuracy_rate)
    else:
        list_shot_accuracy_rates.append(shot_accuracy_rate.text)

    hit_woodwork = soup.find('span', 'allStatContainer stathit_woodwork')
    if (hit_woodwork == None):
        list_hit_woodwork.append(hit_woodwork)
    else:
        list_hit_woodwork.append(hit_woodwork.text)

    big_chances_missed = soup.find('span', 'allStatContainer statbig_chance_missed')
    if (big_chances_missed == None):
        list_big_chances_missed.append(big_chances_missed)
    else:
        list_big_chances_missed.append(big_chances_missed.text)

    assist = soup.find('span', 'allStatContainer statgoal_assist')
    if (assist == None):
        list_assists.append(assist)
    else:
        list_assists.append(assist.text)

    total_pass = soup.find('span', 'allStatContainer stattotal_pass')
    if (total_pass == None):
        list_total_passes.append(total_pass)
    else:
        list_total_passes.append(total_pass.text)

    total_passes_per_game = soup.find('span', 'allStatContainer stattotal_pass_per_game')
    if (total_passes_per_game == None):
        list_total_passes_per_game.append(total_passes_per_game)
    else:
        list_total_passes_per_game.append(total_passes_per_game.text)

    big_chance_created = soup.find('span', 'allStatContainer statbig_chance_created')
    if (big_chance_created == None):
        list_big_chances_created.append(big_chance_created)
    else:
        list_big_chances_created.append(big_chance_created.text)

    cross = soup.find('span', 'allStatContainer stattotal_cross')
    if (cross == None):
        list_crosses.append(cross)
    else:
        list_crosses.append(cross.text)

    yellow_card = soup.find('span', 'allStatContainer statyellow_card')
    if (yellow_card == None):
        list_yellow_cards.append(yellow_card)
    else:
        list_yellow_cards.append(yellow_card.text)

    red_card = soup.find('span', 'allStatContainer statred_card')
    if (red_card == None):
        list_red_cards.append(red_card)
    else:
        list_red_cards.append(red_card.text)

    foul = soup.find('span', 'allStatContainer statfouls')
    if (foul == None):
        list_fouls.append(foul)
    else:
        list_fouls.append(foul.text)

    offside = soup.find('span', 'allStatContainer stattotal_offside')
    if (offside == None):
        list_offside.append(offside)
    else:
        list_offside.append(offside.text)

    tackle = soup.find('span', 'allStatContainer stattotal_tackle')
    if (tackle == None):
        list_tackles.append(tackle)
    else:
        list_tackles.append(tackle.text)

    block_shot = soup.find('span', 'allStatContainer statblocked_scoring_att')
    if (block_shot == None):
        list_blocked_shot.append(block_shot)
    else:
        list_blocked_shot.append(block_shot.text)

    interception = soup.find('span', 'allStatContainer statinterception')
    if (interception == None):
        list_interceptions.append(interception)
    else:
        list_interceptions.append(interception.text)

    clearance = soup.find('span', 'allStatContainer stattotal_clearance')
    if (clearance == None):
        list_clearances.append(clearance)
    else:
        list_clearances.append(clearance.text)

    headed_clearance = soup.find('span', 'allStatContainer stateffective_head_clearance')
    if (headed_clearance == None):
        list_headed_clearances.append(headed_clearance)
    else:
        list_headed_clearances.append(headed_clearance.text)

df = pd.DataFrame({
    'Name': list_players,
    'Country': list_countries,
    'Date of Birth': list_birthday,
    'Height': list_height,
    'Appearance': list_appearances,
    'Wins': list_wins,
    'Losses': list_losses,
    'Goal': list_goals,
    'Assist': list_assists,
    'Goals Per Game': list_goals_per_game,
    'Headed Goals': list_head_goals,
    'Goals With Right Foot': list_goals_with_right_foot,
    'Goals With Left Foot': list_goals_with_left_foot,
    'Penalty Goals': list_penalties_scored,
    'Free Kick Goals': list_free_kicks_scored,
    'Shots': list_shots,
    'Shots On Target': list_shots_on_target,
    'Shooting Accuracy Rate': list_shot_accuracy_rates,
    'Hit Woodwork': list_hit_woodwork,
    'Big Chance Missed': list_big_chances_missed,
    'Total Passes': list_total_passes,
    'Total Passes Per Game': list_total_passes_per_game,
    'Big Chance Created': list_big_chances_created,
    'Crosses': list_crosses,
    'Yellow Cards': list_yellow_cards,
    'Red Cards': list_red_cards,
    'Fouls': list_fouls,
    'Offsides': list_offside,
    'Tackles': list_tackles,
    'Blocked shots': list_blocked_shot,
    'Interceptions': list_interceptions,
    'Clearances': list_clearances,
    'Headed Clearance': list_headed_clearances
})

df.to_csv('../data/forwards.csv', index=False, encoding='utf-8')

print("Scrap Successfully!")
