import pandas as pd
reviews = pd.read_csv(".\input\winemag-data-130k-v2.csv")
print(reviews.head())

renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})
print(renamed.columns)

reindexed = reviews.rename_axis(index='wines')
print(reindexed)