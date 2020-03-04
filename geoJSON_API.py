#https://opendata.arcgis.com/datasets/1564ace0b4f44318ac39920737f9bd07_0.geojson

#https://opendata.arcgis.com/datasets/1564ace0b4f44318ac39920737f9bd07_0.geojson


from arcgis.gis import GIS

anon_gis = GIS()

search_results = anon_gis.content.search(query='title: "MapPLUTO 20*" ')

print(search_results[0])
print(search_results[1])
print(len(search_results))
