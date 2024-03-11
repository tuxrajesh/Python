import pandas as pd
melbourne_file_data = '.\input\melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_data)
# print(melbourne_data.describe()) -- 13580 rows
# filter rows with missing values 13580 rows to 6196 rows
filtered_melbourne_data = melbourne_data.dropna(axis=0)
# choose target
y = filtered_melbourne_data.Price
# choose features
features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[features]

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(random_state=0, max_leaf_nodes=max_leaf_nodes)
    model.fit(train_X, train_y)
    predictions = model.predict(val_X)
    mae = mean_absolute_error(val_y, predictions)
    return mae


melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(X, y)
predictions = melbourne_model.predict(X)
print(mean_absolute_error(y, predictions))

from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(train_X, train_y)
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(random_state=0, max_leaf_nodes=max_leaf_nodes)
    model.fit(train_X, train_y)
    predictions = model.predict(val_X)
    mae = mean_absolute_error(val_y, predictions)
    return mae