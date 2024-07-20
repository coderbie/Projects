import math
from geopy.geocoders import Nominatim

def dist_bw_cities(city1: str, city2: str):
    '''
    Calculates distance between two cities.
    Finds latitude and longitude of the cities using geopy library.
    Uses The Haversine formula to calculate distance.
    '''
    geolocator = Nominatim(user_agent='MyApp')

    location1 = geolocator.geocode(city1)
    location2 = geolocator.geocode(city2)

    if location1 and location2:
        lat1 = math.radians(location1.latitude)
        lon1 = math.radians(location1.longitude)
        lat2 = math.radians(location2.latitude)
        lon2 = math.radians(location2.longitude)
    
    else: 
        raise ValueError('City not found.')

    dlat = lat1-lat2
    dlon = lon1-lon2

    a = ((math.sin(dlat/2)**2)) + math.cos(lat1)*math.cos(lat2)*((math.sin(dlon/2)**2))
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = 6371.0*c

    return round(d, 2)
