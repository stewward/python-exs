#This program shows top 25 tourist attractions in the world map
import folium
import pandas


tourist_data = pandas.read_csv("tourist_data.csv")
lat = list(tourist_data["LAT"])
lon = list(tourist_data["LON"])
name = list(tourist_data["NAME"])


def home_marker(lat, lon):
    map.add_child(folium.Marker(location=[lat, lon], popup = "You are here", icon=folium.Icon(color='blue')))


def elev_color_maker(lat):
    if lat <= 0:
        return 'green'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles=('Stamen Watercolor'))
fg = folium.FeatureGroup(name = "My Map")

for lt, ln, nm in zip(lat, lon, name):
    map.add_child(folium.Marker(location = [lt, ln], popup = str(nm), icon=folium.Icon(color = elev_color_maker(lt))))

map.add_child(fg)
map.save("mapify3.html")