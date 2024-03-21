import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Read the data
X = pd.read_csv('input/train.csv', index_col='Id')
X_test = pd.read_csv('input/test.csv', index_col='Id')

# Remove the rows with missing target, separate the target from parameters
X.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X.SalePrice
X.drop(['SalePrice'], axis=1, inplace=True)

# To keep thigs simple, we'll drop columns with missing values
cols_with_missing = [col for col in X.columns
                     if X[col].isnull().any()]
X.drop(cols_with_missing, axis=1, inplace=True) # axis=1 refers to the columns
X_test.drop(cols_with_missing, axis=1, inplace=True)

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y,
                                                  train_size=0.8, test_size=0.2,
                                                  random_state=0)
# Function for comparing different approaches
def compare_approaches(X_train, X_valid, y_train, y_valid):
    # print('Using Random Forests')
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# Drop columns in training and validation data
drop_X_train = X_train.select_dtypes(exclude=['object'])
drop_X_valid = X_valid.select_dtypes(exclude=['object'])

print("MAE from Approach 1 (Drop categorical variables):")
print(compare_approaches(drop_X_train, drop_X_valid, y_train, y_valid))
# print("Unique values in 'Condition2' column in training data:", X_train['Condition2'].unique())
# print("\nUnique values in 'Condition2' column in validation data:", X_valid['Condition2'].unique())
# Categorical columns in the training data
object_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]

# Columns that can be safely ordinal encoded
good_label_cols = [col for col in object_cols if 
                   set(X_valid[col]).issubset(set(X_train[col]))]
        
# Problematic columns that will be dropped from the dataset
bad_label_cols = list(set(object_cols)-set(good_label_cols))
        
# print('Categorical columns that will be ordinal encoded:', good_label_cols)
# print('\nCategorical columns that will be dropped from the dataset:', bad_label_cols)

from sklearn.preprocessing import OrdinalEncoder
label_X_train = X_train.drop(bad_label_cols, axis=1)
label_X_valid = X_valid.drop(bad_label_cols, axis=1)

ordinal_encoder = OrdinalEncoder()
label_X_train[good_label_cols] = ordinal_encoder.fit_transform(X_train[good_label_cols])
label_X_valid[good_label_cols] = ordinal_encoder.transform(X_valid[good_label_cols])

print("MAE from Approach 2 (Ordinal Encoding):") 
print(compare_approaches(label_X_train, label_X_valid, y_train, y_valid))

# Get number of unique entries in each column with categorical data
# object_nunique = list(map(lambda col: X_train[col].nunique(), object_cols))
# d = dict(zip(object_cols, object_nunique))
# Print number of unique entries by column, in ascending order
# print(sorted(d.items(), key=lambda x: x[1]))

low_cardinality_cols = [col for col in object_cols if X_train[col].nunique() < 10]
high_cardinality_cols = list(set(object_cols) - set(low_cardinality_cols))

from sklearn.preprocessing import OneHotEncoder
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output==False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[low_cardinality_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[low_cardinality_cols]))

OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index

num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_valid.drop(object_cols, axis=1)

OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

OH_X_train.columns = OH_X_train.columns.astype(str)
OH_X_valid.columns = OH_X_valid.columns.astype(str)



