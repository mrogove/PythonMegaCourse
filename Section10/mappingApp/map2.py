import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#init and center map
map = folium.Map([39.721901, -104.994010], zoom_start=5, tiles="Mapbox Bright")

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read()
                                    ,style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
                                                                else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))


map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map2.html")
