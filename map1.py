import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat =list(data["LAT"])
lon =list(data["LON"])
elev =list(data["ELEV"])
name =list(data["NAME"])

def color_producer(elevation):
    
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location= [36.721221, -4.421080], zoom_start=6)

fgv = folium.FeatureGroup(name="Volcanoes")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for lt, ln, el in zip(lat, lon, elev):
    if is_number(el):  # procesar si la elevación es numérica
        fgv.add_child(folium.CircleMarker(
            location=[lt, ln],
            radius=6, 
            popup=str(el) + " meters", 
            fill_color=color_producer(float(el)),
            color="grey",
            fill_opacity=0.7,
            fill=True
        ))
        
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))





map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())  # añadir control de capas

map.save("Map1.html")
