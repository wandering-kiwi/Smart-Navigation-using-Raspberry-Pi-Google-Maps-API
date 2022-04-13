import pandas as pd
from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps

API = 'AIzaSyCNosOBiQiS0nlJMjrKgBOQLUum05Khs94'
geolocator = GoogleV3(api_key=API)

#print(type(geolocator))
name = 'Cambourne, Cambridge : CB23 6FB, Woodfield Ln, Lower Cambourne' 
location = geolocator.geocode(name)

#print(location.address)
#print(location.latitude, location.longitude)
first_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])

#print(first_location)
name = 'Cambourne, Cambridge : Merle Way, Lower Cambourne' 
location = geolocator.geocode(name)

second_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])

name = '20 Sweetentree Way, Lower Cambourne, Cambourne, Cambridge CB23 6FH' 
location = geolocator.geocode(name)

#print(location.address)
#print(location.latitude, location.longitude)
third_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])

name = 'CB23 6FT, Medlar Ln, Lower Cambourne, Cambourne, Cambridge' 
location = geolocator.geocode(name)

#print(location.address)
#print(location.latitude, location.longitude)
fourth_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])

my_locations = pd.concat([first_location, second_location, third_location, fourth_location], ignore_index=True)

#print(my_locations)
p_1 = (my_locations['lat'][0], my_locations['lon'][0])
p_2 = (my_locations['lat'][1], my_locations['lon'][1])
p_3 = (my_locations['lat'][2], my_locations['lon'][2])
p_4 = (my_locations['lat'][3], my_locations['lon'][3])
d=geopy.distance.geodesic(p_1, p_2, p_3, p_4).km

#print(d)
gmap = googlemaps.Client(key=API)

#print(type(gmap))
d_goog = gmap.distance_matrix(p_1, p_2, mode='driving')
d_goog1 = gmap.distance_matrix(p_3, p_4, mode='driving')
#print(d_goog)
b_goog = gmap.distance_matrix(p_1, p_2, mode='bicycling')
b_goog1 = gmap.distance_matrix(p_3, p_4, mode='bicycling')
#print(b_goog)
print("Distance to reach the locations by van: ", (float(d_goog["rows"][0]["elements"][0]["distance"]["text"].strip(" km")) + float(d_goog1["rows"][0]["elements"][0]["distance"]["text"].strip(" km"))), "km")
print("Time it takes to reach the locations by van: ", (float(d_goog["rows"][0]["elements"][0]["duration"]["text"].strip(" mins")) + float(d_goog1["rows"][0]["elements"][0]["duration"]["text"].strip(" mins"))), "mins")
print("Distance to reach the locations by bike: ", round((float(b_goog["rows"][0]["elements"][0]["distance"]["text"].strip(" km")) + float(b_goog1["rows"][0]["elements"][0]["distance"]["text"].strip(" km"))), 2), "km")
print("Time it takes to reach the locations by bike: ", (float(b_goog["rows"][0]["elements"][0]["duration"]["text"].strip(" mins")) + float(b_goog1["rows"][0]["elements"][0]["duration"]["text"].strip(" mins"))), "mins")
print("The distance between the four locations is", round(d, 2), "km")