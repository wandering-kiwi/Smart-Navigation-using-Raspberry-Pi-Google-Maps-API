"""
OUR PROJECT USES THE GOOGLEMAPS API TO CALCULATE HOW FAST IS IS TO DELIVER PACKAGES
BETWEEN DESTINATIONS. WE TAKE ON BOARD TRAFFIC, THE NUMBER OF DELIVERIES AND THE
NEXT DELIVERY POINT. THIS WOULD HELP THE EFFICIENCY OF DELIVERING BY USING SCOOTERS INSTEAD OF VANS.
"""



#IMPORTING ALL LIBARIES FOR GEOGRAPHIC CALCULATIONS
import pandas as pd
from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps
#OUR API KEY *note this key is invalid as the api is a time limited licence, if needed to run this code make another api
API = 'AIzaSyCNosOBiQiS0nlJMjrKgBOQLUum05Khs94'
#SETTING OUR API AS GOOGLEMPAS API AND INITIALISING EVERY FUNCTION
geolocator = GoogleV3(api_key=API)
#OUR FIRST LOCATION AND ALL OF ITS KEY INFORMATION SUCH AS LONGITUDE, LATITUDE AND ADRESS
name = 'CB23 6BT,
 Swansley Ln, 
 Lower Cambourne, ' 
location_1 = geolocator.geocode(name)
first_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])
name = 'Cambourne, Cambridge : CB23 6FB, Woodfield Ln, Lower Cambourne, ' 
#OUR SECOND LOCATION AND ALL OF ITS KEY INFORMATION SUCH AS LONGITUDE, LATITUDE AND ADRESS
location_2 = geolocator.geocode(name)
second_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])
name = 'Cambourne, Cambridge : CB23 6FB, Woodfield Ln, Lower Cambourne' 
#OUR THIRD LOCATION AND ALL OF ITS KEY INFORMATION SUCH AS LONGITUDE, LATITUDE AND ADRESS
location_3 = geolocator.geocode(name)
third_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])
name = 'Cambourne, Cambridge : Merle Way, Lower Cambourne' 
#OUR FOURTH LOCATION AND ALL OF ITS KEY INFORMATION SUCH AS LONGITUDE, LATITUDE AND ADRESS
location_4 = geolocator.geocode(name)

fourth_location = pd.DataFrame([[name, location.address, location.latitude, location.longitude]],
            columns=['name', 'address', 'lat', 'lon'])
name = 'Cambourne, Cambridge : Merle Way, Lower Cambourne' 
            columns=['name', 'address', 'lat', 'lon'])
 #CALCULATING THE TIME IT TAKES FOR ALL FOUR LOCATIONS ON A CAR AND A BIKE
timeittakes = pd.findtime("car", "bike", my_locations)
my_locations = pd.concat([first_location, second_location, third_location, fourth_location], ignore_index=True)
timefordelivery = pd.calculatetime(my_locations, sum(location_1, location_2, location_3, location_4))
print(my_locations)
#INITIALISING ALL LOCATIONS
p_1 = (my_locations['lat'][0], my_locations['lon'][0])
p_2 = (my_locations['lat'][1], my_locations['lon'][1])
p_3 = (my_locations['lat'][2], my_locations['lon'][4])
p_4 = (my_locations['lat'][4], my_locations['lon'][2])
num_deliv = my_locations
d=geopy.distance.geodesic(p_1, p_2, p_3, p_4).km
#IMPLEMENTING OUR FORMULA
calculation1 = (num_deliv * timeittakes[0]) + timefordelivery
calculation2 = (timeittakes[1] * num_deliv) + timefordelivery
#print(d)
print()
#gmap = googlemaps.Client(key=API)

#OUTPUTTING ALL OF OUR RESULTS
#VAN TIME VS SCOOTER TIME RESULTS
print("VAN TIME =", calculation1, "> SCOOTER TIME", calculation2)
d_goog = mode='driving'
c_goog = mode = "cycling"
#OUTPUTTING CALCULATONS OF ALL TIMES WITH DRIVING AND CYCLING
print(p_1.calculate(d_goog))
print(p_2.calculate(c_goog))
print(p_3.calculate(d_goog))
print(p_4.calculate(c_goog))
