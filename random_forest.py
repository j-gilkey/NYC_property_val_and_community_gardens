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

def get_years_since_mod(row):

    if row['yearalter2'] > 0:
        return (int(row['year']) - int(row['yearalter2']))

    if row['yearalter1'] > 0:
        return (int(row['year']) - int(row['yearalter1']))

    else:
        return row['age_at_sale']


def get_train_test_split():
    df = sales_data_eda.sales_eda_wrapper()

    columns_to_keep = ['year', 'schooldist', 'numfloors', 'unitsres', 'yearbuilt', 'yearalter1', 'yearalter2', 'sale_price',  'landuse',  'lotarea', 'lottype',  'histdist', 'landmark', 'builtfar', 'residfar', 'lat', 'lng']

    df = df.loc[:, columns_to_keep]

    df['age_at_sale'] = df.apply(lambda row: get_buidling_age(row))
    df['years_since_mod'] = df.apply(lambda row: get_years_since_mod(row))

    dummy_columns= ['year', 'schooldist', 'landuse', 'lottype']
    columns_to_drop = ['yearalter1', 'yearalter2', 'yearbuilt']


    print(df.head)


get_train_test_split()
