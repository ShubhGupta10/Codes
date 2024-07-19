from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode("DELHI")
print(location.address)
print((location.latitude, location.longitude))
