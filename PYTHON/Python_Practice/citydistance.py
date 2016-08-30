import math
from geopy.geocoders import Nominatim

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees).
    Source: http://gis.stackexchange.com/a/56589/15183
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    km = 6367 * c
    return "Distance between two cities is : " + str(km) + " KM"

def main():
    geolocator = Nominatim()
    #get first city
    print 'Type the first City: '
    cityA = raw_input()
    
    #get second city
    print 'Type the second city: '
    cityB = raw_input()
    location1 = geolocator.geocode(cityA)
    location2 = geolocator.geocode(cityB)

    print haversine(location1.longitude, location1.latitude, location2.longitude, location2.latitude)

main()