import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix
import final_dataframe_prep
from sklearn.metrics import mean_squared_error

pd.set_option('display.max_columns', None)

#df = pd.read_csv('data/prepped_for_model.csv' )
#df = pd.read_csv('data/prepped_for_model_under_3mill.csv' )
df = pd.read_csv('data/prepped_for_model_logged_price.csv' )

print(df.head)
