import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer

data = pd.read_csv(".\\input\\melb_data.csv")
y = data.Price

melb_predictors =data.drop(['Price'], axis=1)
X = melb_predictors.select_dtypes(exclude=['object'])

# print(melb_predictors.head())
# print(X.head())

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(X_train, y_train)
    predictions = model.predict(X_valid)
    return mean_absolute_error(y_valid, predictions)

# Approach 1: Drop columns with missing values
# get names of colums with missing values
cols_with_missing_values = [col for col in X_train.columns if X_train[col].isnull().any()]
print(cols_with_missing_values)

# drop columns with missing values in the training and validation data
reduced_X_train = X_train.drop(cols_with_missing_values, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing_values, axis=1)

print("MAE from Approach 1: Drop columns with missing values.")
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))

# Approach 2: Imputation
simple_imputter = SimpleImputer()
imputed_X_train = pd.DataFrame(simple_imputter.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(simple_imputter.transform(X_valid))

print("MAE from Approach 2: Imputation.")
print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))

# Approach 3: An extension to imputation
X_train_plus = X_train.copy()
X_valid_plus = X_valid.copy()

# Make new columns indicating what will be imputed
for col in cols_with_missing_values:
    X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
    X_valid_plus[col + "_was_missing"] = X_valid_plus[col].isnull()
    
imputed_X_train_plus = pd.DataFrame(simple_imputter.fit_transform(X_train_plus))
imputed_X_valid_plus = pd.DataFrame(simple_imputter.transform(X_valid_plus))

print("MAE from Approach 3: Extenstion to Imputation.")
print(score_dataset(imputed_X_train_plus, imputed_X_valid_plus, y_train, y_valid))

print(X_train.shape)

missing_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])

