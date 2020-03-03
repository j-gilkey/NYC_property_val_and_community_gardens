import pandas as pd
import math

pd.set_option('display.max_columns', None)

df = pd.read_csv('data/data_with_predictions_1.csv' )

df['price'] = df.apply(lambda row: math.exp(row['log_price']), axis=1)
df['predicted_price'] = df.apply(lambda row: math.exp(row['predicted_log']), axis=1)

df['error'] = df.apply(lambda row: row['price'] - row['predicted_price'], axis=1)
df['abs_error'] = df.apply(lambda row: abs(row['error']), axis=1)

print(df['abs_error'].mean())
print(df['price'].mean())

print(df.nlargest(200, 'abs_error'))
#print(df.head)
