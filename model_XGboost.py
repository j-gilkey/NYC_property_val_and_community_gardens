import xgboost as xgb
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import final_dataframe_prep
import grid_search

pd.set_option('display.max_columns', None)

#df = pd.read_csv('data/prepped_for_model.csv' )
#df = pd.read_csv('data/prepped_for_model_under_3mill.csv' )
df = pd.read_csv('data/prepped_for_model_logged_price.csv' )
X  = df.drop('log_price', axis=1)
Y  = df['log_price']
X_train, X_test,y_train,y_test = final_dataframe_prep.get_train_test_split(df, 'log_price')

# xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,
#                 max_depth = 5, alpha = 10, n_estimators = 10)
#
# xg_reg.fit(X_train,y_train)
#
# preds = xg_reg.predict(X_test)
#
# rmse = np.sqrt(mean_squared_error(y_test, preds))
# print("RMSE: %f" % (rmse))


def grid_search_XG(X_train, X_test, y_train, y_test):
    xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,
                    max_depth = 5, alpha = 10, n_estimators = 100)

    param_grid = {
        'learning_rate': [0.1, 0.2],
        'max_depth': [2,5],
        'min_child_weight': [1, 3],
        'subsample': [0.5, 0.9],
        'n_estimators': [100,200],
    }

    grid_search.grid_search(xg_reg, param_grid, X_train, X_test, y_train, y_test, scoring = 'neg_mean_absolute_error')


grid_search_XG(X_train, X_test, y_train, y_test)
