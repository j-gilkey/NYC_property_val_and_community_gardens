import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv('man_vacant_parks_df.csv' )

df_location = df.loc[:, ['address', 'latitude', 'longitude']]

df_location.to_csv('df_location.csv', index=False)

print(df_location.head)
