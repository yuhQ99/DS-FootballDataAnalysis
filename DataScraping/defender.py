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
wins = []
losses = []
goals = []
clean_sheets = []
goal_concededs = []
tackles = []
tackle_successes = []
last_man_tackles = []
block_shots = []
interceptions = []
clearances = []
headed_clearances = []
clearance_off_lines = []
recoveries = []
duel_wons = []
duel_losts = []
won_contests = []
aerial_wons = []
aerial_losts = []
own_goals = []
error_lead_to_goals = []
assists = []
total_passes = []
total_pass_per_games = []
big_chances = []
crosses = []
cross_accuracies = []
through_balls = []
accurate_long_balls = []
yellow_cards = []
red_cards = []
fouls = []
offsides = []
headed_goals = []
goals_with_right_foots = []
goals_with_left_foots = []
hit_woodworks = []

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
    if(td.text == 'Defender'):
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
        list_height.append(0)

for link in links:
    driver.get(link)
    time.sleep(5)

    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")

    name = soup.find('div', 'name t-colour')
    players.append(name.text)

    appearance = name.findNext('span', 'allStatContainer statappearances')
    appearances.append(appearance.text)

    goal = appearance.findNext('span', 'allStatContainer statgoals')
    goals.append(goal.text)

    win = goal.findNext('span', 'allStatContainer statwins')
    wins.append(win.text)

    loss = win.findNext('span', 'allStatContainer statlosses')
    losses.append(loss.text)

    cs = loss.findNext('span', 'allStatContainer statclean_sheet')
    clean_sheets.append(cs.text)

    goal_conceded = cs.findNext('span', 'allStatContainer statgoals_conceded')
    goal_concededs.append(goal_conceded.text)

    tackle = goal_conceded.findNext('span', 'allStatContainer stattotal_tackle')
    tackles.append(tackle.text)

    tackle_success = tackle.findNext('span', 'allStatContainer stattackle_success')
    tackle_successes.append(tackle_success.text)

    last_man_tackle = tackle_success.findNext('span', 'allStatContainer statlast_man_tackle')
    last_man_tackles.append(last_man_tackle.text)

    block_shot = last_man_tackle.findNext('span', 'allStatContainer statblocked_scoring_att')
    block_shots.append(block_shot.text)

    interception = block_shot.findNext('span', 'allStatContainer statinterception')
    interceptions.append(interception.text)

    clearance = interception.findNext('span', 'allStatContainer stattotal_clearance')
    clearances.append(clearance.text)

    headed_clearance = clearance.findNext('span', 'allStatContainer stateffective_head_clearance')
    headed_clearances.append(headed_clearance.text)

    clearance_off_line = headed_clearance.findNext('span', 'allStatContainer statclearance_off_line')
    clearance_off_lines.append(clearance_off_line.text)

    recovery = clearance_off_line.findNext('span', 'allStatContainer statball_recovery')
    recoveries.append(recovery.text)

    duel_won = recovery.findNext('span', 'allStatContainer statduel_won')
    duel_wons.append(duel_won.text)

    duel_lost = duel_won.findNext('span', 'allStatContainer statduel_lost')
    duel_losts.append(duel_lost.text)

    won_contest = duel_lost.findNext('span', 'allStatContainer statwon_contest')
    won_contests.append(won_contest.text)

    aerial_won = won_contest.findNext('span', 'allStatContainer stataerial_won')
    aerial_wons.append(aerial_won.text)

    aerial_lost = aerial_won.findNext('span', 'allStatContainer stataerial_lost')
    aerial_losts.append(aerial_lost.text)

    own_goal = aerial_lost.findNext('span', 'allStatContainer statown_goals')
    own_goals.append(own_goal.text)

    error_lead_to_goal = own_goal.findNext('span', 'allStatContainer staterror_lead_to_goal')
    error_lead_to_goals.append(error_lead_to_goal.text)

    assist = error_lead_to_goal.findNext('span', 'allStatContainer statgoal_assist')
    assists.append(assist.text)

    total_pass = assist.findNext('span', 'allStatContainer stattotal_pass')
    total_passes.append(total_pass.text)

    total_pass_per_game = total_pass.findNext('span', 'allStatContainer stattotal_pass_per_game')
    total_pass_per_games.append(total_pass_per_game.text)

    big_chance = total_pass_per_game.findNext('span', 'allStatContainer statbig_chance_created')
    big_chances.append(big_chance.text)

    cross = big_chance.findNext('span', 'allStatContainer stattotal_cross')
    crosses.append(cross.text)

    cross_accuracy = cross.findNext('span', 'allStatContainer statcross_accuracy')
    cross_accuracies.append(cross_accuracy.text)

    through_ball = cross_accuracy.findNext('span', 'allStatContainer stattotal_through_ball')
    through_balls.append(through_ball.text)

    accurate_long_ball = through_ball.findNext('span', 'allStatContainer stataccurate_long_balls')
    accurate_long_balls.append(accurate_long_ball.text)

    yellow_card = accurate_long_ball.findNext('span', 'allStatContainer statyellow_card')
    yellow_cards.append(yellow_card.text)

    red_card = yellow_card.findNext('span', 'allStatContainer statred_card')
    red_cards.append(red_card.text)

    foul = red_card.findNext('span', 'allStatContainer statfouls')
    fouls.append(foul.text)

    offside = foul.findNext('span', 'allStatContainer stattotal_offside')
    offsides.append(offside.text)

    headed_goal = offside.findNext('span', 'allStatContainer statatt_hd_goal')
    headed_goals.append(headed_goal.text)

    goals_with_right_foot = headed_goal.findNext('span', 'allStatContainer statatt_rf_goal')
    goals_with_right_foots.append(goals_with_right_foot.text)

    goals_with_left_foot = goals_with_right_foot.findNext('span', 'allStatContainer statatt_lf_goal')
    goals_with_left_foots.append(goals_with_left_foot.text)

    hit_woodwork = goals_with_left_foot.findNext('span', 'allStatContainer stathit_woodwork')
    hit_woodworks.append(hit_woodwork.text)

df = pd.DataFrame({'Name': players,
                   'Country': list_countries,
                   'Date of Birth': list_birthday,
                   'Height': list_height,
                   'Appearance': appearances,
                   'Wins': wins,
                   'Losses': losses,
                   'Clean Sheet': clean_sheets,
                   'Goal': goals,
                   'Assist': assists,
                   'Goal Conceded': goal_concededs,
                   'Tackle': tackles,
                   'Tackle Success Rate': tackle_successes,
                   'Last Man Tackle': last_man_tackles,
                   'Blocked Shots': block_shots,
                   'Interceptions': interceptions,
                   'Clearances': clearances,
                   'Headed Clearance': headed_clearances,
                   'Clearances Off Line': clearance_off_lines,
                   'Recoveries': recoveries,
                   'Duels won': duel_wons,
                   'Duels lost': duel_losts,
                   'Successful 50/50s': won_contests,
                   'Aerial Battles Won': aerial_wons,
                   'Aerial Battles Lost': aerial_losts,
                   'Own Goals': own_goals,
                   'Errors Leading To Goal': error_lead_to_goals,
                   'Passes': total_passes,
                   'Passes Per Match': total_pass_per_games,
                   'Big Chances Created': big_chances,
                   'Crosses': crosses,
                   'Cross Accuracy %': cross_accuracies,
                   'Through Balls': through_balls,
                   'Accurate Long Balls': accurate_long_balls,
                   'Yellow Cards': yellow_cards,
                   'Red Cards': red_cards,
                   'Fouls': fouls,
                   'Offsides': offsides,
                   'Headed Goals': headed_goals,
                   'Goals With Right Foot': goals_with_right_foots,
                   'Goals With Left Foot': goals_with_left_foots,
                   'Hit Woodwork': hit_woodworks})

df.to_csv('../data/defenders.csv', index=False, encoding='utf-8')

print("Scrap Successfully!")