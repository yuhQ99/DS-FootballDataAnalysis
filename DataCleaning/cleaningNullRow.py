import pandas as pd

df = pd.read_csv("../DataScraping/forwards.csv")

df_filtered = df[df['Appearance'] > 0]

df_filtered.to_csv('../data/forwards.csv', index=False, encoding='utf-8')

df = pd.read_csv("../DataScraping/midfielders.csv")
df_filtered = df[df['Appearance'] > 0]

df_filtered.to_csv('../data/midfielders.csv', index=False, encoding='utf-8')

df = pd.read_csv("../DataScraping/defenders.csv")

df_filtered = df[df['Appearance'] > 0]

df_filtered.to_csv('..data/defenders.csv', index=False, encoding='utf-8')

df = pd.read_csv("../DataScraping/goalkeepers.csv")

df_filtered = df[df['Appearance'] > 0]

df_filtered.to_csv('../data/goalkeepers.csv', index=False, encoding='utf-8')