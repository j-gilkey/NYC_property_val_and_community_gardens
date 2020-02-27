import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import SQL_functions
import re
import garden_locator

pd.set_option('display.max_columns', None)

def check_for_non_num(row):
    block = row['lot']

    if re.match('\D', block):
        return 'yes'

    else:
        return 'no'


def create_sales_df():

    data = SQL_functions.get_sales()
    df = pd.DataFrame(data, columns = ['sale_id', 'neighborhood', 'block', 'lot', 'address', 'sale_price', 'sale_date', 'apt_number', 'unit_type', 'year'])
    df = df.set_index('sale_id')

    #df['contains_non_numeral'] = df.apply(lambda row: check_for_non_num(row), axis = 1)
    #df = df[df['contains_non_numeral']=='yes']

    return df

def filter_residential(df):
    pluto_data = SQL_functions.get_PLUTO()
    pluto_df = pd.DataFrame(pluto_data, columns = ['lot_id', 'block', 'lot', 'cd', 'zipcode', 'address', 'zonedist1', 'schooldist', 'splitzone', 'bldgclass', 'landuse', 'ownername', 'lotarea',
                                    'lottype', 'numfloors', 'unitsres', 'yearbuilt', 'yearalter1', 'yearalter2', 'histdist', 'landmark', 'builtfar', 'residfar', 'lat', 'lng'])
    pluto_df = pluto_df.set_index('lot_id')

    #print(pluto_df.shape)

    #print(pluto_df['landuse'])

    pluto_df = pluto_df[pluto_df['landuse'].isin(['1.0', '2.0', '3.0'])]

    #print(pluto_df.shape)

    #print(df.shape)

    trimmed_sales = pd.merge(df, pluto_df,how="inner", on=['block', 'lot'])

    return trimmed_sales

def count_plot(df, to_plot):
    #a count plot to show the class distrobution within the dataset
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')

    ax = sns.countplot(x=to_plot, data=df)
    #ax.set_ylabel('Recipe Count')
    #ax.set_xlabel('Cuisine')
    plt.show()

def multi_hist_plot(df_1, df_2, to_plot, label_1='dist_1', label_2='dist_2'):
    #takes a dataframe and a column to create a hist plot on
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    hist_1 = sns.distplot(df_1[to_plot].astype(float), kde = False, label=label_1)
    hist_2 = sns.distplot(df_2[to_plot].astype(float), kde = False, label=label_2)
    # print(stats.kurtosis(list(df[to_plot])))
    # print(stats.skew(list(df[to_plot])))
    #hist_serial.set_xlabel('Log Salary')
    #hist_serial.set_xlabel('Trees per sq Mile')
    plt.legend()
    plt.show()

def hist_plot(df, to_plot):
    #takes a dataframe and a column to create a hist plot on
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    hist_serial = sns.distplot(df[to_plot].astype(float), kde = False)
    # print(stats.kurtosis(list(df[to_plot])))
    # print(stats.skew(list(df[to_plot])))
    #hist_serial.set_xlabel('Log Salary')
    #hist_serial.set_xlabel('Trees per sq Mile')
    plt.show()

def scatter_plot(X, Y, df):
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    ax = sns.scatterplot(x=df[X], y=df[Y], data=df)
    plt.show()

def joint_plot(X, Y, df):
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    g = sns.jointplot(X, Y, data=df,
                  kind="kde", space=0,)
    plt.show()


def sales_eda_wrapper():

    df = create_sales_df()
    #print(df.shape)
    df = filter_residential(df)
    #print(df.shape)

    df_units = df[df['unit_type'] == 'apartment']
    df_units = garden_locator.find_nearby_gardens(df_units)
    #print(df_units.shape)
    #df_units = df_units[df_units['sale_price'] < 3000000]
    df_units['log_price'] = df_units.apply(lambda row: np.log(row['sale_price']), axis =1)
    #df_buildings = df[df['unit_type'] == 'whole_building']
    #df_buildings = df_buildings[df_buildings['sale_price'] < 14000000]
    #df_2009_units = df_units[df_units['year'] == '2009']
    #df_2013_units = df_units[df_units['year'] == '2013']
    #df_2018_units = df_units[df_units['year'] == '2018']

    #hist_plot(df_units, 'log_price')

    #scatter_plot('lat', 'lng', df_units)
    #joint_plot('lat', 'lng', df_2018_units)

    #multi_hist_plot(df_2013_units, df_2018_units, 'sale_price', '2013', '2018')

    #count_plot(df_zero, 'year')

    return df_units


#sales_eda_wrapper()
