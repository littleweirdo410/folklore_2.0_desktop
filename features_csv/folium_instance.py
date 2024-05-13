import folium
from folium.plugins import MarkerCluster
import pandas as pd

data = pd.read_csv('doc.txt', encoding='windows-1251')
lat = data["geometry/coordinates/1"]
long = data["geometry/coordinates/0"]

district = data["properties/Attributes/District"]
address = data["properties/Attributes/Address"]
areas = data["properties/Attributes/AdmArea"]

class MyMap:
    def __init__(self):
        self.map1 = folium.Map(location=[55.754099333918056, 37.62077354050015], zoom_start=8)


all_areas = []
for i in areas:
    if i not in all_areas:
        all_areas.append(i)

central_area = MarkerCluster(name=all_areas[0]).add_to(map1)
eastern_area = MarkerCluster(name=all_areas[1]).add_to(map1)
southeastern_area = MarkerCluster(name=all_areas[2]).add_to(map1)
western_area = MarkerCluster(name=all_areas[3]).add_to(map1)
zelenograd_area = MarkerCluster(name=all_areas[4]).add_to(map1)
northern_area = MarkerCluster(name=all_areas[5]).add_to(map1)
northeastern_area = MarkerCluster(name=all_areas[6]).add_to(map1)
northwestern_area = MarkerCluster(name=all_areas[7]).add_to(map1)
southern_area = MarkerCluster(name=all_areas[8]).add_to(map1)
southwestern_area = MarkerCluster(name=all_areas[9]).add_to(map1)
troitsky_area = MarkerCluster(name=all_areas[10]).add_to(map1)
novomoskovsk_area = MarkerCluster(name=all_areas[11]).add_to(map1)

full_addresses = [areas[i] + ', ' + district[i] + ', ' + address[i] for i in range(60)]
ignore_indices = [2, 9, 11, 12, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 57, 58, 59]

for i in range(60):
    if areas[i] == all_areas[0]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(central_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(central_area)
    if areas[i] == all_areas[1]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(eastern_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(eastern_area)
    if areas[i] == all_areas[2]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(southeastern_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(southeastern_area)
    if areas[i] == all_areas[3]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(western_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(western_area)
    if areas[i] == all_areas[4]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(zelenograd_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(zelenograd_area)
    if areas[i] == all_areas[5]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(northern_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(northern_area)
    if areas[i] == all_areas[6]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(northeastern_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(northeastern_area)
    if areas[i] == all_areas[7]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(northwestern_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(northwestern_area)
    if areas[i] == all_areas[8]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(southern_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(southern_area)
    if areas[i] == all_areas[9]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(southwestern_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(southwestern_area)
    if areas[i] == all_areas[10]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(troitsky_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(troitsky_area)
    if areas[i] == all_areas[11]:
        if i in ignore_indices:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='orange')).add_to(novomoskovsk_area)
        else:
            folium.Marker(location=[lat[i], long[i]], tooltip=full_addresses[i], icon=folium.Icon(color='green')).add_to(novomoskovsk_area)

map1.save("map1.html")
