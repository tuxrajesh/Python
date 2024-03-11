import pandas as pd
reviews = pd.read_csv(".\\input\\winemag-data-130k-v2.csv", index_col = 0)
pd.set_option('display.max_rows', 5)

# >> Learning

# print(reviews)
# print(reviews['country'][129970])
# print(reviews.iloc[1:3,0])
# print(reviews.loc[reviews.country.isin(['Italy', 'France'])])

# >> Exercise
# desc = reviews.description
# first_descrition = reviews.description.iloc[0]
# indices = [0, 1, 10, 100]
# columns = ['country', 'province', 'region_1', 'region_2']
# result = reviews.loc[indices, columns]

# columns = ['country', 'variety']
# df = reviews.loc[:100, columns]
# print(df)
# 
# review_points_mean = reviews.points.mean()
# result = reviews.points.map(lambda p: p - review_points_mean)
# print(result)

# def remean_points(row):
#     row.points = row.points - review_points_mean
#     return row

# reviews.apply(remean_points, axis='columns')
# def price_point_ratio(row):
#     row.price = row.points/row.price
#     return row

# reviews_price_point_ratio = reviews.apply(price_point_ratio, axis='columns')
# indices = [0, 1, 129969, 129970]
# columns = ['title', 'price']
# print(reviews_price_point_ratio.loc[indices, columns])

# bargain_wine = reviews_price_point_ratio.title[reviews_price_point_ratio.price == reviews_price_point_ratio.price.max()]
# print(bargain_wine)

# bargain_idx = (reviews.points / reviews.price).idxmax()
# bargain_wine = reviews.loc[bargain_idx, 'title']
# print(bargain_wine)

# tropical_instances = reviews.description.map(lambda d: "tropical" in d.lower())
# fruity_instances = reviews.description.map(lambda d: "fruity" in d.lower())
# descriptor_counts = pd.Series([tropical_instances.sum(), fruity_instances.sum()], index=['tropical', 'fruity'])

# print(descriptor_counts)

# """
# We'd like to host these wine reviews on our website, but a rating 
# system ranging from 80 to 100 points is too hard to 
# understand - we'd like to translate them into simple star ratings. 
# A score of 95 or higher counts as 3 stars, 
# a score of at least 85 but less than 95 is 2 stars. 
# Any other score is 1 star.

# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.

# Create a series star_ratings with the number of stars corresponding to each review in the dataset.
# """
# def redef_points(row):
#     if row.country == "Canada":
#         return 3
#     elif row.points >= 95:
#         return 3
#     elif row.points >= 85:
#         return 2
#     else:
#         return 1
    
# star_ratings = reviews.apply(redef_points, axis='columns')
# print(star_ratings)

result = reviews.groupby('points').points.count()
print(result)
print(reviews.points.value_counts())