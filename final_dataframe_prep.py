import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
import garden_locator
import sales_data_eda

pd.set_option('display.max_columns', None)

def get_buidling_age(row):
    age = int(row['year']) - int(row['yearbuilt'])
    return age

def get_years_since_mod(row):

    if row['yearalter2'] > 0:
        return (int(row['year']) - int(row['yearalter2']))

    if row['yearalter1'] > 0:
        return (int(row['year']) - int(row['yearalter1']))

    else:
        return row['age_at_sale']

def make_dummies(df, column, set_prefix = 'dummy'):
    dummy = pd.get_dummies(df[column],prefix = set_prefix, drop_first=True)
    df = pd.concat([df, dummy], axis = 1)
    return df

def model_prep():
    df = sales_data_eda.sales_eda_wrapper()

    columns_to_keep = ['year', 'schooldist', 'numfloors', 'unitsres', 'yearbuilt', 'yearalter1', 'yearalter2', 'sale_price',  'landuse',  'lotarea', 'lottype',  'histdist', 'landmark', 'builtfar', 'residfar','distance_to_garden', 'lat', 'lng']

    df = df.loc[:, columns_to_keep]

    df['age_at_sale'] = df.apply(lambda row: get_buidling_age(row), axis = 1)
    df['years_since_mod'] = df.apply(lambda row: get_years_since_mod(row), axis = 1)

    dummy_columns= ['year', 'schooldist', 'landuse', 'lottype']
    df = make_dummies(df, 'year', 'sale_year')
    df = make_dummies(df, 'schooldist', 'sch_dist')
    df = make_dummies(df, 'landuse', 'lnd_use')
    df = make_dummies(df, 'lottype', 'lot_type')

    columns_to_drop = ['yearalter1', 'yearalter2', 'yearbuilt','year', 'schooldist', 'landuse', 'lottype']
    df = df.drop(columns_to_drop, axis=1)
    df = df[df['sale_price'] < 3000000]

    df['log_price'] = df.apply(lambda row: np.log(row['sale_price']), axis =1)
    df = df.drop('sale_price', axis=1)

    print(df.head)
    return(df)


def get_train_test_split(df, y_column_name):
    X = df.drop(columns=[y_column_name])
    y = df[y_column_name]

    X_train, X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)
    x_y_dict ={'X_train' : X_train, 'X_test' : X_test, 'y_train': y_train, 'y_test' : y_test}
    return(X_train, X_test,y_train,y_test)

def heat_corr(df):
    fig = plt.figure()
    #plt.clear()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    corr = df.corr()
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    ax = sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True)
    #ax.set_title(name)
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    plt.show()

#df = model_prep()
#heat_corr(df)
#df.to_csv('data/prepped_for_model_logged_price.csv', index=False)
