import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('figure', max_open_warning = 0)

dataframes = pd.read_csv("./Clubs.csv", error_bad_lines=False)
barWidth = 0.5
Goals = dataframes["Goals"]
Losses = dataframes["Losses"]
Wins = dataframes["Wins"]
Name = dataframes["Name"]
Game = Wins.add(Losses)
GoalPerGame = Goals.div(Game)
GoalPerWin = Goals.div(Wins)
y_pos = np.arange(len(Name))
r2 = [x*3 + barWidth*3  for x in y_pos]
r3 = [x*3 + barWidth for x in y_pos]
r4 = [x + 0.5 for x in r3]

plt.bar(r3,GoalPerGame, color = 'black', edgecolor = 'black', label= 'Goals Per Game')
plt.bar(r2,GoalPerWin, color = 'red', edgecolor = 'black', label='Goals Per Win')
plt.xticks(r4, Name, rotation=90)
plt.subplots_adjust(bottom=0.4, top=0.99)
plt.legend()
plt.show()