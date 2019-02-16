import csv
import json
import math

query = 'json object'

radius = '1 mile'

result = 'json file of longs and lats and content description'

vehicle_info = open('vehicles.csv', mode='r')
reader = csv.reader(vehicle_info)
#query_to_dict = json.loads(query)


def find_relevant_incidents(lng, lat, radius):
    lat_per_mile = radius/69
    long_per_mile = radius/(69.172*math.cos(lat*math.pi/180))

    min_lat = lat - lat_per_mile
    max_lat = lat + lat_per_mile
    min_long = long - long_per_mile
    max_long = long + long_per_mile


