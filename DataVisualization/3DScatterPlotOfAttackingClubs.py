from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from scipy import stats, optimize, interpolate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(25, 25))
ax1 = fig.add_subplot(111, projection='3d')

X = []
Y = []
Z = []
names = []
df = pd.read_csv("../data/Clubs.csv")

goals = df['Goals']

for goal in goals:
    X.append(int(goal))

X = np.array(X)
shots = df['Shots']

for shot in shots:
    Y.append(int(shot))

Y = np.array(Y)

passes = df['Passes']

for p in passes:
    p = p.replace(",", "")
    Z.append(int(p))
Z = np.array(Z)

n = df['Unnamed: 0']
for name in n:
    names.append(name)

ax1.scatter(X, Y, Z, c='b', marker='o')

for name, x, y, z in zip(names, X, Y, Z):
    label = '%s' % (str(name))
    ax1.text(x, y, z, label, fontsize=7)

plt.title('Attacking of Premier League Clubs')

ax1.set_xlabel('Goals')
ax1.set_ylabel('Shots')
ax1.set_zlabel('Passes')

ax1.get_proj = lambda: np.dot(Axes3D.get_proj(ax1), np.diag([2, 2, 2, 2]))

plt.show()
