import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map([39.721901, -104.994010], zoom_start=5, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[39.721901,-104.994010],popup="Productive Denver Location",icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[40.3094215,-105.6708506],popup="White Walkers spotted here",icon=folium.Icon(color='blue')))

for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=(lt,ln),popup="This is a VOLCANO",icon=folium.Icon(color='red')))


map.add_child(fg)

map.save("Map1.html")
