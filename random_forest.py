import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix
import final_dataframe_prep
from sklearn.metrics import mean_squared_error

pd.set_option('display.max_columns', None)

#df = pd.read_csv('data/prepped_for_model.csv' )
#df = pd.read_csv('data/prepped_for_model_under_3mill.csv' )
df = pd.read_csv('data/prepped_for_model_logged_price.csv' )

#print(df.head)

#X_train, X_test,y_train,y_test = final_dataframe_prep.get_train_test_split(df, 'sale_price')
X_train, X_test,y_train,y_test = final_dataframe_prep.get_train_test_split(df, 'log_price')

def plot_feature_importances(model, X_train):
    n_features = X_train.shape[1]
    plt.figure(figsize=(8,8))
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), X_train.columns.values)
    plt.xlabel('Feature importance')
    plt.ylabel('Feature')
    plt.show()

def random_forest(X_train, X_test, y_train, y_test, max_depth = 5, n_estimators = 100):
    forest = RandomForestRegressor(n_estimators=n_estimators, max_depth= max_depth, max_features = 2)
    forest.fit(X_train, y_train)

    clasPred = forest.predict(X_test)
    #print(clasPred)
    #print(accuracy_score(y_test, clasPred))
    print(mean_squared_error(y_test, clasPred, squared=False))

    #plot_feature_importances(forest, X_train)


random_forest(X_train, X_test, y_train, y_test)
