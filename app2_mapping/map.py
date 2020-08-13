import folium as fo
import pandas as pd


def color_producer(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'


map=fo.Map(tiles='Stamen Terrain')
fgv=fo.FeatureGroup(name="volcanoes")
coordinates =pd.read_csv("4.1 Volcanoes.txt.txt")

lat=list(coordinates['LAT'])
print(type(lat[0]))
lon=list(coordinates['LON'])
names=list(coordinates['NAME'])
timeframe=list(coordinates['TIMEFRAME'])
elev=list(coordinates['ELEV'])
print(coordinates.columns)

for lt,ln,name,el in zip(lat,lon,names,elev):
    fgv.add_child(fo.CircleMarker(location=[lt,ln],popup=f'{str(el)} m',radius=14,fill_color=color_producer(el),
                                 color='grey',fill_opacity=0.7))
fgp=fo.FeatureGroup(name='Population')
fgp.add_child(fo.GeoJson(data=open('13.1 world.json.json','r',encoding= 'utf-8-sig').read(),
                        style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 100000000 else
                        'orange' if x['properties']['POP2005'] < 200000000 else 'red'}))
map.add_child(fgp)
map.add_child(fgv)
map.add_child(fo.LayerControl())
map.save("map1.html")
