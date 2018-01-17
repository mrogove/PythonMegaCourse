import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map([39.721901, -104.994010], zoom_start=5, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[39.721901,-104.994010],popup="Productive Denver Location",icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[40.3094215,-105.6708506],popup="White Walkers spotted here",icon=folium.Icon(color='blue')))

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln]
                              ,popup=folium.Popup(str(el), parse_html=True)
                              ,icon=folium.Icon(color='red')))


map.add_child(fg)

map.save("Map1.html")
