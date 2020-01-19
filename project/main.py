import folium

map = folium.Map(location=[38.58, -99.09])

feature_group = folium.FeatureGroup(name="Map")
feature_group.add_child(folium.Marker(location=[38.7, -98.95], popup="Custom Marker", icon=folium.Icon(color="green")))

map.add_child(feature_group)

map.save("../html/map.html")
