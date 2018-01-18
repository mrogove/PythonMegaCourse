import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#init and center map
map = folium.Map([39.721901, -104.994010], zoom_start=5, tiles="Mapbox Bright")

def get_color(elevation):
    if elevation < 1000:
        return('lightgreen')
    elif elevation < 3000:
        return('orange')
    else:
        return('darkred')

fg = folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln]
                              ,popup=folium.Popup(str(el)+" meters", parse_html=True)
                              ,fill_color=get_color(el)
                              ,radius=6,color='grey',fill_opacity=0.7, fill=True))

fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read()
                                    ,style_function=lambda x: {'fillColor':'yellow'}))


map.add_child(fg)
map.save("Map2.html")
