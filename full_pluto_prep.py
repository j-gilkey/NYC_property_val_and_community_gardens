import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
import garden_locator
import sales_data_eda
import SQL_functions
import final_dataframe_prep


def full_prep():

    #this function sets up the entire Manhattan PLUTO dataset to be passed into the model for predictions
    #to be used after the model is fit with sales data

    pluto_data = SQL_functions.get_PLUTO()
    #call the SQL function to get PLUTO data

    df = pd.DataFrame(pluto_data, columns = ['lot_id', 'block', 'lot', 'cd', 'zipcode', 'address', 'zonedist1', 'schooldist', 'splitzone', 'bldgclass', 'landuse', 'ownername', 'lotarea',
                                    'lottype', 'numfloors', 'unitsres', 'yearbuilt', 'yearalter1', 'yearalter2', 'histdist', 'landmark', 'builtfar', 'residfar', 'lat', 'lng'])
    #cast it to a pandas dataframe and specify column attr_names

    df = df.set_index('lot_id')
    #set the set_index

    df = df[df['landuse'].isin(['1.0', '2.0', '3.0'])]
    #only get exclusively residential buildings using the landuse column

    df['year'] = 2018
    #set the "purchase year" of the lot to the most recent year of data, IE 2018

    columns_to_keep = ['year', 'schooldist', 'numfloors', 'unitsres', 'yearbuilt', 'yearalter1', 'yearalter2', 'landuse',  'lotarea', 'lottype',  'histdist', 'landmark', 'builtfar', 'residfar', 'lat', 'lng']
    df = df.loc[:, columns_to_keep]
    #trim down to only columns needed for the model

    df = df[df.schooldist != '10.0']
    df = df[df.lottype != 8]
    df = df[df.lottype != 9]
    #the above distric and lot type were not present in the training data and therefore these rows will be excluded

    df = garden_locator.find_nearby_gardens(df)
    #use the find_nearby_gardens funtion to add distance_to_garden into the dataframe


    df = final_dataframe_prep.make_dummies(df, 'year', 'sale_year')
    df = final_dataframe_prep.make_dummies(df, 'schooldist', 'sch_dist')
    df = final_dataframe_prep.make_dummies(df, 'landuse', 'lnd_use')
    df = final_dataframe_prep.make_dummies(df, 'lottype', 'lot_type')
    #create dummy columns

    df['age_at_sale'] = df.apply(lambda row: final_dataframe_prep.get_buidling_age(row), axis = 1)
    #create age_at_sale column

    df['years_since_mod'] = df.apply(lambda row: final_dataframe_prep.get_years_since_mod(row), axis = 1)
    #create years_since_mod column


    columns_to_drop = ['yearalter1', 'yearalter2', 'yearbuilt','year', 'schooldist', 'landuse', 'lottype']
    df = df.drop(columns_to_drop, axis=1)
    #drop final unneeded columns

    columns = ['numfloors', 'unitsres', 'lotarea', 'histdist', 'landmark', 'builtfar',
       'residfar', 'distance_to_garden', 'lat', 'lng', 'age_at_sale',
       'years_since_mod', 'sale_year_2010', 'sale_year_2011', 'sale_year_2012',
       'sale_year_2013', 'sale_year_2014', 'sale_year_2015', 'sale_year_2016',
       'sale_year_2017', 'sale_year_2018', 'sch_dist_2.0', 'sch_dist_3.0',
       'sch_dist_4.0', 'sch_dist_5.0', 'sch_dist_6.0', 'lnd_use_2.0',
       'lnd_use_3.0', 'lot_type_1', 'lot_type_2', 'lot_type_3', 'lot_type_4',
       'lot_type_5', 'lot_type_6', 'lot_type_7']

    df = df[columns]
    #ensure proper column ordering

    return df

#full_df = full_prep()
