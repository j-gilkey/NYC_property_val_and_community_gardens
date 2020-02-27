import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

# lots_df = pd.read_csv('data/man_df.csv')
# garden_df = pd.read_csv('data/df_location_2.csv')
#
# columns_to_keep = ['borough', 'block', 'lot', 'cd', 'zipcode', 'address', 'zonedist1', 'splitzone', 'bldgclass', 'landuse', 'ownertype', 'ownername', 'lotarea', 'bldgarea', 'latitude', 'longitude']
#
# lots_df = lots_df.loc[:, columns_to_keep].dropna()
# garden_df = garden_df.loc[:, columns_to_keep].dropna()
#
# print(lots_df.head)
# print(garden_df.shape)

def find_nearby_gardens(lots_df):

    garden_df = pd.read_csv('data/df_location_2.csv')

    gar_loc_df = garden_df.loc[:, ['latitude', 'longitude']]
    lots_loc_df = lots_df.loc[:, ['lat', 'lng']]

    neigh = NearestNeighbors(1)
    neigh.fit(gar_loc_df)

    #print(lots_loc_df.iloc[:2])

    #print(neigh.kneighbors(lots_loc_df, return_distance=True))

    lots_df['distance_to_garden'] = [(i[0]*364286) for i in neigh.kneighbors(lots_loc_df, return_distance=True)[0]]

    return lots_df

#lots_df = find_nearby_gardens(garden_df, lots_df)
#print(lots_df.head)
