import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import SQL_functions
import re
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
    columns_to_drop = ['yearalter1', 'yearalter2', 'yearbuilt']
    df = df.drop(columns_to_drop, axis=1)

    df = make_dummies(df, 'year', 'sale_year')
    df = make_dummies(df, 'schooldist', 'sch_dist')
    df = make_dummies(df, 'landuse', 'lnd_use')
    df = make_dummies(df, 'lottype', 'lot_type')

    #print(df.head)
    return(df)


#df = model_prep()
#df.to_csv('data/prepped_for_model.csv', index=True)
