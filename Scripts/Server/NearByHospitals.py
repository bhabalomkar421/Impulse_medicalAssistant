# api ===  AIzaSyD7elb1-Nv2LsezcVO-6X8R_qZU0H6SZJc
from googleplaces import GooglePlaces, types, lang
import requests
import json

API_KEY = 'AIzaSyDJ_PwyHDWaEpc7fpSZ7iYXaBFz32oZBhc'

# Initialising the GooglePlaces constructor
google_places = GooglePlaces(API_KEY)

# call the function nearby search with
# the parameters as longitude, latitude,
# radius and type of place which needs to be searched of
# type can be HOSPITAL, CAFE, BAR, CASINO, etc
query_result = google_places.nearby_search(
    # lat_lng ={'lat': 46.1667, 'lng': -1.15},
    lat_lng={'lat': 28.4089, 'lng': 77.3178},
    radius=5000,
    # types =[types.TYPE_HOSPITAL] or
    # [types.TYPE_CAFE] or [type.TYPE_BAR]
    # or [type.TYPE_CASINO])
    types=[types.TYPE_HOSPITAL])

# If any attributions related
# with search results print them
if query_result.has_attributions:
    print(query_result.html_attributions)


# # Iterate over the search results
# for place in query_result.places:
#     # print(type(place))
#     # place.get_details()
#     print(place.name)
#     print("Latitude", place.geo_location['lat'])
#     print("Longitude", place.geo_location['lng'])
#     print()
