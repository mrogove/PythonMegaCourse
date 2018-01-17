import folium
map = folium.Map([39.721901, -104.994010], zoom_start=10, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[39.721901, -104.994010]
                            , popup='Productive Denver Location'
                            , icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")
