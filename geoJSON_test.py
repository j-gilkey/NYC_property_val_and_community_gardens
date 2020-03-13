import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import geojsonio
import pprint
import json
import SQL_functions

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

pluto_EV = gpd.read_file('data/geojson/pluto_EV.geojson')
pred_df = pd.read_csv('data/all_with_predictions_unlogged.csv')
pred_df = pred_df[['lat', 'lng', 'distance_to_garden', 'predicted']]
pluto_data = SQL_functions.get_PLUTO()
location_df = pd.DataFrame(pluto_data, columns = ['lot_id', 'block', 'lot', 'cd', 'zipcode', 'address', 'zonedist1', 'schooldist', 'splitzone', 'bldgclass', 'landuse', 'ownername', 'lotarea',
                                'lottype', 'numfloors', 'unitsres', 'yearbuilt', 'yearalter1', 'yearalter2', 'histdist', 'landmark', 'builtfar', 'residfar', 'lat', 'lng'])
location_df = location_df.set_index('lot_id')

location_df = location_df[['block', 'lot','lat', 'lng']]
location_df = location_df.astype({'block':'int64'})
location_df = location_df.astype({'lot':'int64'})
location_df = location_df.astype({'lat':'float'})
location_df = location_df.astype({'lng':'float'})
print(pred_df.dtypes)

#location_df = int()
#print(location_df.dtypes)

print(location_df.columns)

pluto_EV = pluto_EV.merge(location_df, how='left', on=['block', 'lot'])
pluto_EV = pluto_EV.merge(pred_df, how='left', on=['lat', 'lng'])

#merged_location = pd.merge(pluto_EV, location_df, how='left', on=['block', 'lot'])

print(pluto_EV.shape)
print(type(pluto_EV))

pluto_EV = pluto_EV.dropna()

pluto_EV = pluto_EV.to_json()
geojsonio.display(pluto_EV)
#pluto_EV = pluto_EV.dropna()
#print(pluto_EV.shape)


#pluto_EV_contents = open('data/geojson/pluto_EV.geojson').read()

#geojsonio.display(pluto_EV_contents)

#pluto_EV_dict = json.loads(pluto_EV_contents)
#pprint.pprint(pluto_EV_dict)
#for i in pluto_EV_dict['features']:
#    print(i)

#print(pluto_EV_dict['type'])
#print(type(pluto_EV_dict['features']))

#pprint.pprint(pluto_EV_contents)

#geojsonio.display(pluto_EV_contents)

# pluto_man = gpd.read_file('data/geojson/pluto_manhattan.geojson' )
#
# #print(type(pluto_man))
# #print(pluto_man.head)
#
# #pluto_man = pluto_man.to_json()
# #print(type(pluto_man))
#
# pluto_EV = gpd.read_file('data/geojson/pluto_EV.geojson' )
# #print(type(pluto_EV))
# print(pluto_EV.head)
#
# #pluto_EV = pluto_EV.to_json()
# #print(type(pluto_EV))
# pluto_man.plot()
# plt.show()

#geojsonio.display(pluto_EV)

# pluto_EV = gpd.read_file('data/geojson/pluto_EV.geojson' )
# pluto_LES = gpd.read_file('data/geojson/pluto_LES.geojson' )
#
# pluto_EV = gpd.read_file('data/geojson/pluto_EV.geojson' )
# pluto_EV['neighborhood'] = 'EV'
# pluto_LES = gpd.read_file('data/geojson/pluto_LES.geojson' )
# pluto_LES['neighborhood'] = 'LES'
# pluto_EV = pluto_EV.drop('borough', axis=1)
# pluto_EV = pluto_EV.drop('appbbl', axis=1)
#
# #merged = pluto_EV.merge
#
# print(pluto_EV.head)
#
# #print(pluto_LES.head())
#
# pluto_combined = gpd.GeoDataFrame(pd.concat([pluto_LES, pluto_EV],ignore_index=True))
# print(type(pluto_combined))
#
# #print(pluto_combined.head())
#
# #pluto.plot(column='lot')
#
# #pluto_EV = pluto_EV.to_json()
# pluto_LES = pluto_LES.to_json()
# #print(pluto_LES)
# pluto_combined = pluto_combined.to_json()
# #print(pluto_combined)
#
# #geojsonio.display(pluto_combined)
