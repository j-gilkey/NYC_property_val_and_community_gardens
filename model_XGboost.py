import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error
import pandas as pd
import final_dataframe_prep
import grid_search
import math
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

#df = pd.read_csv('data/prepped_for_model.csv' )
#df = pd.read_csv('data/prepped_for_model_under_3mill.csv' )
df = pd.read_csv('data/prepped_for_model_unlogged_price.csv' )
X  = df.drop('sale_price', axis=1)
Y  = df['sale_price']
X_train, X_test,y_train,y_test = final_dataframe_prep.get_train_test_split(df, 'sale_price')

def XGboost_reg(X_train, X_test, y_train, y_test):
    xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.2,
    max_depth = 5, alpha = 10, n_estimators = 200, subsample=.9)

    xg_reg.fit(X_train,y_train)

    preds = xg_reg.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, preds))
    mae = mean_absolute_error(y_test, preds)
    print("RMSE: %f" % (rmse))
    print("MAE: %f" % (mae))

    return xg_reg

def predict_all_properties(model):

    pluto_df = pd.read_csv('data/full_pluto_prepped.csv' )

    pluto_df['predicted_log'] = model.predict(pluto_df)
    #pluto_df['predicted_val'] = df.apply(lambda row: math.exp(row['predicted_log']), axis = 1)

    #print(pluto_df.head)

    return pluto_df

def plot_feature_importances(model, X_train):
    n_features = X_train.shape[1]
    plt.figure(figsize=(8,8))
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), X_train.columns.values)
    plt.xlabel('Feature importance')
    plt.ylabel('Feature')
    plt.show()



#xg_reg = XGboost_reg(X_train, X_test, y_train, y_test)

#plot_feature_importances(xg_reg, X_train)
#print(y_test.mean())




#pluto_df = predict_all_properties(xg_reg)
#pluto_df.to_csv('data/all_with_predictions_unlogged.csv', index=False)

# df['predicted_log'] = xg_reg.predict(X)
#
# df.to_csv('data/data_with_predictions_2.csv', index=False)

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
        'max_depth': [3,6,9],
        'min_child_weight': [1, 2, 3],
        'subsample': [ 0.7, 0.9],
        'n_estimators': [150, 180, 200],
        'eta': [0.01, 0.2, 0.3]
    }

    grid_search.grid_search(xg_reg, param_grid, X_train, X_test, y_train, y_test, scoring = 'neg_root_mean_squared_error')


grid_search_XG(X_train, X_test, y_train, y_test)



'''
Grid Search found the following optimal parameters:
learning_rate: 0.2
max_depth: 5
min_child_weight: 1
n_estimators: 200
subsample: 0.9

'''


'''
Grid Search found the following optimal parameters:
eta: 0.01
learning_rate: 0.2
max_depth: 3
min_child_weight: 3
n_estimators: 200
subsample: 0.9
'''
