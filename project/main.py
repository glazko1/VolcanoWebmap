import folium
import pandas

map = folium.Map(location=[38.58, -99.09])

feature_group = folium.FeatureGroup(name="Map")

df = pandas.read_csv("../data/volcanoes.txt")
for index, row in df.iterrows():
    feature_group.add_child(folium.Marker(location=[row["LAT"], row["LON"]],
                                          popup=row["NAME"],
                                          icon=folium.Icon(color="green")))

map.add_child(feature_group)

map.save("../html/map.html")
