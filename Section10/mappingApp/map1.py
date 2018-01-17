import folium
map = folium.Map([39.721901, -104.994010], zoom_start=5, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[39.721901,-104.994010],popup="Productive Denver Location",icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[40.3094215,-105.6708506],popup="White Walkers spotted here",icon=folium.Icon(color='blue')))

for coordinates in [[38.2,-99.1],[39.2,-97.1]]:
    fg.add_child(folium.Marker(location=coordinates,popup="This is a marker",icon=folium.Icon(color='red')))


map.add_child(fg)

map.save("Map1.html")
