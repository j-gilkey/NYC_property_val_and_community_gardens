import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix
import final_dataframe_prep
import model_general_functions
from sklearn.metrics import mean_squared_error, mean_absolute_error

def get_train_test_split(logged=False):
    #get train test split division of either logged or unlogged data

    if logged:
        df = pd.read_csv('data/prepped_for_model_logged_price.csv' )
        X_train, X_test,y_train,y_test = final_dataframe_prep.get_train_test_split(df, 'log_price')
    else:
        df = pd.read_csv('data/prepped_for_model.csv' )
        X_train, X_test,y_train,y_test = final_dataframe_prep.get_train_test_split(df, 'sale_price')
    return X_train, X_test,y_train,y_test


def random_forest(X_train, X_test, y_train, y_test, max_depth = 5, n_estimators = 100):
    #instantiates a random forest model with the input parapmeters and then fits it to the data
    forest = RandomForestRegressor(n_estimators=n_estimators, max_depth= max_depth, max_features = 2)
    forest.fit(X_train, y_train)

    clasPred = forest.predict(X_test)
    print(mean_absolute_error(y_test, clasPred))

    #model_general_functions.plot_feature_importances(forest, X_train)

    return forest

def grid_search_forest(X_train, X_test, y_train, y_test, param_grid, max_depth = 5, n_estimators = 100):
    #perform gridsearch on random forest
    forest = RandomForestRegressor(n_estimators=n_estimators, max_depth= max_depth, max_features = 2)

    model_general_functions.grid_search(forest, param_grid, X_train, X_test, y_train, y_test, scoring = 'neg_mean_absolute_error')

def forest_wrapper():
    X_train, X_test,y_train,y_test = get_train_test_split()
    #get the split

    param_grid = {
        'max_features':[2,4,10],
        'max_depth': [2,5],
        'n_estimators': [30, 60, 90]
    }

    grid_search_forest(X_train, X_test, y_train, y_test, param_grid)
    #grid search on it

#forest_wrapper()
