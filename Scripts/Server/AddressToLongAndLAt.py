from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Home
lat = 19.0643595
longitude = 73.0027549


def AddressToGeocoordinates():
    geolocator = Nominatim(user_agent="Elysian")
    location = geolocator.geocode("Terna Nerul Navi Mumbai")
    print(location.address)
    print((location.latitude, location.longitude))


def DistanceBetweenGeoCoordinates():
    newport_ri = (41.49008, -71.312796)
    cleveland_oh = (41.499498, -71.395391)
    Miles2Kilometer(geodesic(newport_ri, cleveland_oh).miles)

# for under 5 km first three number should be same
# Increasing the 3rd number in either cases adds extra 5-8 kms


def Miles2Kilometer(miles):
    conversion_factor = 1.60934
    kilometers = miles * conversion_factor
    print(kilometers)


if __name__ == '__main__':
    DistanceBetweenGeoCoordinates()
    # AddressToGeocoordinates()
