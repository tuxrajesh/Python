import pandas as pd
reviews = pd.read_csv(".\\input\\winemag-data-130k-v2.csv", index_col=0)
# pd.set_option('display.max_rows', 5)

# reviews_written = reviews.groupby("taster_twitter_handle").taster_twitter_handle.count()
# print(reviews_written)

# best_rating_per_price = reviews.groupby(['price'])['points'].agg("max").sort_index()
# print(best_rating_per_price)

# price_extremes = reviews.groupby('variety').price.agg([min, max])
# print(price_extremes)

# sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
# print(sorted_varieties)

# reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()
# print(reviewer_mean_ratings)

# country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
# print(country_variety_counts)

dtype = reviews.points.dtype
print(dtype)

n_missing_prices = reviews.price.isnull().sum()
print(n_missing_prices)

reviews_by_region = reviews['region_1'].fillna('Unknown').value_counts().sort_values(ascending=False)
print(reviews_by_region)