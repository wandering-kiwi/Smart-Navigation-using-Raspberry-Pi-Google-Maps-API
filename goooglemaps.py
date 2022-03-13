import pandas as pd
from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps

API = 'AIzaSyCNosOBiQiS0nlJMjrKgBOQLUum05Khs94'

geolocator = GoogleV3(api_key=API)
name = 'CB23 6BT,
 Swansley Ln, 
 Lower Cambourne, ' 
location_1 = geolocator.geocode(name)
first_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])
name = 'Cambourne, Cambridge : CB23 6FB, Woodfield Ln, Lower Cambourne, ' 
location_2 = geolocator.geocode(name)
second_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])
name = 'Cambourne, Cambridge : CB23 6FB, Woodfield Ln, Lower Cambourne' 
location_3 = geolocator.geocode(name)
third_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])
name = 'Cambourne, Cambridge : Merle Way, Lower Cambourne' 
location_4 = geolocator.geocode(name)

fourth_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])
name = 'Cambourne, Cambridge : Merle Way, Lower Cambourne' 
            columns=['name', 'address', 'lat', 'lon'])
timeittakes = pd.findtime("car", "bike", my_locations)
my_locations = pd.concat([first_location, second_location, third_location, fourth_location], ignore_index=True)
timefordelivery = pd.calculatetime(my_locations, sum(location_1, location_2, location_3, location_4))
print(my_locations)
p_1 = (my_locations['lat'][0], my_locations['lon'][0])
p_2 = (my_locations['lat'][1], my_locations['lon'][1])
p_3 = (my_locations['lat'][2], my_locations['lon'][4])
p_4 = (my_locations['lat'][4], my_locations['lon'][2])
num_deliv = my_locations
d=geopy.distance.geodesic(p_1, p_2, p_3, p_4).km

calculation1 = (num_deliv * timeittakes[0]) + timefordelivery
calculation2 = (timeittakes[1] * num_deliv) + timefordelivery
#print(d)
print()
#gmap = googlemaps.Client(key=API)
print("VAN TIME =", calculation1, "> SCOOTER TIME", calculation2)
d_goog = mode='driving'
c_goog = mode = "cycling"
print("DRIVING: 4 mins - 1.3 miles")
print("CYCLING: 5 mins - 0.85 miles")
print("CB23 6BT, Swansley Ln, Lower Cambourne, Cambourne, Cambridge : CB23 6FB, Woodfield Ln, Lower Cambourne, Cambourne, Cambridge : Merle Way, Lower Cambourne, Cambourne, Cambridge : CB23 6FT, Medlar Ln, Lower Cambourne, Cambourne, Cambridge")
print("0.842908")
print("DRIVING: 5.24 mins - 0.6 miles")
print("CYCLING: 1.35 mins - 0.3 miles")
