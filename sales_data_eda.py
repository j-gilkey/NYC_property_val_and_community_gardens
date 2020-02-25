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



def clean_sales_data(df):
    #takes a raw sales csv and standardizes it

    df = df.rename(columns=lambda x: x.strip())
    #remove any whitespace from column names

    columns_to_keep = ['NEIGHBORHOOD', 'BLOCK', 'LOT', 'ADDRESS', 'SALE PRICE', 'SALE DATE']
    df = df.loc[:, columns_to_keep]
    #prune down to only the columns we are interested in

    df['SALE PRICE'] = df.apply(lambda row: int(row['SALE PRICE'].strip('$').replace(',', '')), axis = 1)
    #remove dollar sign and comma characters from price before converting it to an int

    df['apt_number'] = df.apply(lambda row: get_apt_number(row), axis = 1)
    df['ADDRESS'] = df.apply(lambda row: get_address(row), axis = 1)
    #split out address and apartment apt_number

    df['unit_type'] = df.apply(lambda row: classify_type(row), axis = 1)
    #then use that to classify whether or not a particular sale was of a whole building

    df = df.dropna()
    #drop rows with missing values

    df = df[df['SALE PRICE']!='0']
    #remove any sale where no money was exchanged

    return df

# sales_2019_df = pd.read_csv('data/rollingsales_manhattan_1.csv' )
#
# sales_2019_df = clean_sales_data(sales_2019_df)
# print(sales_2019_df.head)

sales_2018_df = pd.read_csv('data/2018_manhattan.csv')

sales_2018_df = clean_sales_data(sales_2018_df)
print(sales_2018_df.head)

print(sales_2018_df.dtypes)
