import folium
import pandas

volcano_data = pandas.read_csv("volcano_data.txt")
lat = list(volcano_data["LAT"])
lon = list(volcano_data["LON"])
elev = list(volcano_data["ELEV"])
name = list(volcano_data["NAME"])

#Takes an parameter called elevation... 
def elev_color_maker(elevation):
    if elevation < 1000:
       return 'green'
    elif 1000 <= elevation < 3000:
       return 'orange'
    else:
       return 'red'


#target=_blank means it opens link in new tab 
#Heigh: %s is the elevation
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
 
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el, name in zip(lat, lon, elev, name):
   iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
   fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = elev_color_maker(el))))
 
map.add_child(fg)
map.save("mapify2.html")