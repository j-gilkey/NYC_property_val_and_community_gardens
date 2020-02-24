import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('pluto_20v1.csv' )

#garden_df = pd.read_csv('garden_df.csv' )

#manhattan_df = pd.read_csv('man_df.csv' )

def count_plot(df,to_count):
    #a count plot to show the class distribution within the dataset
    fig = plt.figure()
    plt.style.use('seaborn')
    sns.set_palette('colorblind')
    ax = sns.countplot(x=to_count, data=df, order = ['BK', 'BX', 'MN', 'QN', 'SI'])
    #ax.set_ylabel('Recipe Count')
    #ax.set_xlabel('Cuisine')
    plt.show()

count_plot(df,'borough')
