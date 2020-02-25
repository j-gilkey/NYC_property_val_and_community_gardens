import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

sales_df = pd.read_csv('data/rollingsales_manhattan_1.csv' )

columns_to_keep = ['borough', 'block', 'lot', 'cd', 'zipcode', 'address', 'zonedist1', 'splitzone', 'bldgclass', 'landuse', 'ownertype', 'ownername', 'lotarea', 'bldgarea', 'latitude', 'longitude']

#sales_df = sales_df.loc[:, columns_to_keep].dropna()

#print(sales_df.shape)
