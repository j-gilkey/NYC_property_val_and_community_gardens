import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import SQL_functions

pd.set_option('display.max_columns', None)


def populate_lots():

    lots_df = pd.read_csv('data/man_df.csv')

    #print(lots_df.shape)

    columns_to_keep = ['block', 'lot', 'cd', 'zipcode', 'address', 'zonedist1', 'schooldist', 'splitzone', 'bldgclass', 'landuse', 'ownername', 'lotarea', 'lottype', 'numfloors', 'unitsres', 'yearbuilt', 'yearalter1', 'yearalter2', 'histdist', 'landmark', 'builtfar', 'residfar', 'latitude', 'longitude']

    lots_df = lots_df.loc[:, columns_to_keep]
    lots_df['landmark'] = lots_df['landmark'].notna()
    lots_df['histdist'] = lots_df['histdist'].notna()
    lots_df = lots_df.dropna()
    #print(lots_df.head)
    #print(lots_df.shape)

    df_tuples = lots_df.itertuples(index = False)

    tuple_list =[]

    for tuple in df_tuples:
        #print(tuple)
        new_tuple = [val for val in tuple]
        new_tuple = (*new_tuple,)
        SQL_functions.insert_PLUTO_lot(new_tuple)
        #tuple_list.append((*new_tuple,))

    #SQL_functions.insert_PLUTO_lot(tuple_list)


#populate_lots()
