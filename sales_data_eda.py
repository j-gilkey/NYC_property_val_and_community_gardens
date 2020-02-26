import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
import SQL_functions

pd.set_option('display.max_columns', None)

def get_apt_number(row):
    address = row['ADDRESS'].split(',')

    if len(address)>1:
        return address[1]
    else:
        return 'no_apt_num'

def get_address(row):
    address = row['ADDRESS'].split(',')

    return address[0]

def classify_type(row):

    if row['apt_number'] == 'no_apt_num':
        return 'whole_building'
    else:
        return 'apartment'

def get_sale_amount(row):
    sale_amount =  row['SALE PRICE']
    #print(sale_amount)
    sale_amount = sale_amount.strip()
    sale_amount = sale_amount.strip('$\\t')
    sale_amount = sale_amount.replace(',', '')
    sale_amount = sale_amount.replace('-', '0')
    #print(sale_amount)
    sale_amount = int(float(sale_amount))

    return sale_amount

def get_year(row):
    date =  row['SALE DATE']
    year = '20' + date[-2:]

    return year


def clean_sales_data(df):
    #takes a raw sales csv and standardizes it

    df = df.rename(columns=lambda x: x.strip())
    #remove any whitespace from column names

    columns_to_keep = ['NEIGHBORHOOD', 'BLOCK', 'LOT', 'ADDRESS', 'SALE PRICE', 'SALE DATE']
    df = df.loc[:, columns_to_keep]
    #prune down to only the columns we are interested in

    df['SALE PRICE'] = df.apply(lambda row: get_sale_amount(row), axis = 1)
    #remove dollar sign and comma characters from price before converting it to an int

    df['apt_number'] = df.apply(lambda row: get_apt_number(row), axis = 1)
    df['ADDRESS'] = df.apply(lambda row: get_address(row).rstrip(), axis = 1)
    #split out address and apartment apt_number

    df['NEIGHBORHOOD'] = df.apply(lambda row: row['NEIGHBORHOOD'].rstrip(), axis = 1)\
    #strip trailing whitespace off neighborhood

    df['unit_type'] = df.apply(lambda row: classify_type(row), axis = 1)
    #then use that to classify whether or not a particular sale was of a whole building

    df['year'] = df.apply(lambda row: get_year(row), axis = 1)
    #then use that to classify whether or not a particular sale was of a whole building

    df = df.dropna()
    #drop rows with missing values

    df = df[df['SALE PRICE']>0]
    #remove any sale where no money was exchanged

    return df



def make_tuples(df):

    tuples = list(df.itertuples(index=False, name=None))
    return tuples

def sales_wrapper():
    years = range(2009,2019)

    for year in years:

        sales_df = pd.read_csv('data/' +str(year)+ '_manhattan.csv')

        #print(sales_df.dtypes)

        sales_df = clean_sales_data(sales_df)

        tuples = make_tuples(sales_df)

        print(tuples[0])

        SQL_functions.insert_sale(tuples)

    #print(tuples[0])

sales_wrapper()
