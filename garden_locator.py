import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

def find_nearby_gardens(lots_df):
    #takes in a dataframe that contains 'lat' and 'lng' columns representing lattitude and longitude coordinates
    #for each of those points this function adds the distance in feet to the nearest manhattan comunity garden

    garden_df = pd.read_csv('data/df_location_2.csv')
    #read in the list of gardens

    gar_loc_df = garden_df.loc[:, ['latitude', 'longitude']]
    lots_loc_df = lots_df.loc[:, ['lat', 'lng']]
    #trim both dataframes to only contain latitude and longitude columns, allowing it to be fed into KNN

    neigh = NearestNeighbors(1)
    neigh.fit(gar_loc_df)
    #instantiate NN and fit it to the garden locations

    lots_df['distance_to_garden'] = [(i[0]*364286) for i in neigh.kneighbors(lots_loc_df, return_distance=True)[0]]
    # calculate and add the distance_to_garden column for each row in the input df

    return lots_df

#lots_df = find_nearby_gardens(garden_df, lots_df)
#print(lots_df.head)
