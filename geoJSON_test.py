import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import geojsonio
import pprint
import json

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

overall_dict = {'type': 'FeatureCollection', 'features':[]}


#pluto_EV = gpd.read_file('data/geojson/pluto_EV.geojson' )

pluto_EV_contents = open('data/geojson/pluto_EV.geojson').read()
pluto_LES_contents = open('data/geojson/pluto_EV.geojson').read()

neighborhoods = [pluto_EV_contents, pluto_LES_contents]

for neigh in neighborhoods:
    pluto_dict_holder = json.loads(neigh)
    features = pluto_dict_holder['features']
    for feature in features:
        overall_dict['features'].append(feature)

print(overall_dict)
print(pluto_dict_holder)
final_json = json.dumps(overall_dict)
print(final_json)
print(pluto_EV_contents)

geojsonio.display(pluto_EV_contents)

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
