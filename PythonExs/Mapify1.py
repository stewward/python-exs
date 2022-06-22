import folium
import pandas

volcano_data = pandas.read_csv("volcano_data.txt")
lat = list(volcano_data["LAT"])
lon = list(volcano_data["LON"])
elev = list(volcano_data["ELEV"])
name = list(volcano_data["NAME"])


map = folium.Map(location=[40.793426023081174, -111.88893245265274], zoom_start = 5, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name = "Temple Square")

#Add marker
#map.add_child(folium.Marker(location=[31.191036986865683, 121.49435366729072], popup = "Shanghai Art Museum (中华艺术宫)", icon=folium.Icon(color='red')))
#map.add_child(folium.Marker(location=[43.52759497774049, -79.64936647329942], popup = "Home", icon=folium.Icon(color='blue')))

#Add marker
#for coords in [[31.191036986865683, 121.49435366729072] , [43.52759497774049, -79.64936647329942]]:
    #map.add_child(folium.Marker(location = coords, popup = "Shanghai Art Museum (中华艺术宫)", icon=folium.Icon(color='red')))


#for lt, ln, el, nm in zip(lat, lon, elev, name):
#    map.add_child(folium.Marker(location = [lt, ln], popup = str(nm) + "\n" + str(el) + "m", icon=folium.Icon(color='red')))


for lt, ln, el, nm in zip(lat, lon, elev, name):
    map.add_child(folium.Marker(location = [lt, ln], popup = str(nm) + "\n" + str(el) + "m", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("map1.html")