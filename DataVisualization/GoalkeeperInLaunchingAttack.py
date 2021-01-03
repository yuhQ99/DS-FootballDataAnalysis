import pandas as pd
import seaborn as sns 
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

dataframes = pd.read_csv("./goalkeepers.csv")
longPass = dataframes["Long Ball"]
Appear = dataframes["Appearance"]
LongPassPG = longPass.div(Appear)
sns.regplot(x=dataframes["Total Pass Per Game"], y=LongPassPG, scatter_kws={"color":"red","alpha":0.3,"s":500})
plt.ylabel('Long Pass Per Game')
plt.show()