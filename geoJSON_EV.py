import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import geojsonio
import pprint
import json
import SQL_functions

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

def get_EV_map_df():
    #this reads in some data files and outputs an interactive browser-based map of East Village buildings in the dataset

    pluto_EV = gpd.read_file('data/geojson/pluto_EV.geojson')
    #read in just East Village locations

    pred_df = pd.read_csv('data/all_with_predictions_unlogged.csv')
    pred_df = pred_df[['lat', 'lng', 'distance_to_garden', 'predicted']]
    #read in every property with predictions and trim to relevant columns


    pluto_data = SQL_functions.get_PLUTO()
    location_df = pd.DataFrame(pluto_data, columns = ['lot_id', 'block', 'lot', 'cd', 'zipcode', 'address', 'zonedist1', 'schooldist', 'splitzone', 'bldgclass', 'landuse', 'ownername', 'lotarea',
                                    'lottype', 'numfloors', 'unitsres', 'yearbuilt', 'yearalter1', 'yearalter2', 'histdist', 'landmark', 'builtfar', 'residfar', 'lat', 'lng'])
    location_df = location_df.set_index('lot_id')
    #read in full puto set, name columns and set index

    location_df = location_df[['block', 'lot','lat', 'lng']]
    location_df = location_df.astype({'block':'int64'})
    location_df = location_df.astype({'lot':'int64'})
    location_df = location_df.astype({'lat':'float'})
    location_df = location_df.astype({'lng':'float'})
    #trim to only the columns we're interested in displaying on the map
    #then convert each column to the desired type

    pluto_EV = pluto_EV.merge(location_df, how='left', on=['block', 'lot'])
    pluto_EV = pluto_EV.merge(pred_df, how='left', on=['lat', 'lng'])
    #left merge the east village dataset with location and predictions

    pluto_EV = pluto_EV.dropna()
    #drop NA values
    pluto_EV = pluto_EV.to_json()
    #convery to json


    geojsonio.display(pluto_EV)
    #finally use geojsonio to display in browser



#pluto_EV = get_EV_map_df()
