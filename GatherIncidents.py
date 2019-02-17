import csv
import json
import math
from collections import defaultdict

"""
    The "Haversine" formula:
    Calculates the great circle distance in miles between two locations given their respective
    latitudes and longitudes in degrees.
    Formula from: https://en.wikipedia.org/wiki/Haversine_formula
"""
def haversine(long1, lat1, long2, lat2):
    # assuming longs and lats passed in are in degrees:
    # convert latitudes and longitudes to radians
    long1_radians = long1 * math.pi/180
    lat1_radians = lat1 * math.pi/180
    long2_radians = long2 * math.pi/180
    lat2_radians = lat2 * math.pi/180

    # get the difference between the two locations and convert to radians
    long_difference = (long2 - long1)*math.pi/180
    lat_difference = (lat2 - lat1)*math.pi/180

    # the radius of the earth in miles
    earth_radius = 3956

    great_circle_distance = earth_radius * 2 * math.asin(math.sqrt(math.sin(lat_difference/2)**2 +
    math.cos(lat1_radians) * math.cos(lat2_radians) * math.sin(long_difference/2)**2))

    return great_circle_distance

"""
    Gets all relevant incidents within a specified radius given a latitude and longitude in degrees.
    A dictionary of dictionaries is returned where the outer dictionary key is the incident id and
    the inner dictionary contains information such as incident category, date, description,
    latitude and longitude.
"""
def find_relevant_incidents(lng, lat, radius):
    # read vehicle csv
    vehicle_info = open('vehicles.csv', mode='r')

    # skip header row of the csv file
    has_header = csv.Sniffer().has_header(vehicle_info.read(1024))
    vehicle_info.seek(0)
    reader = csv.reader(vehicle_info)
    if has_header:
        next(reader)

    relevant_incidents = defaultdict(dict)
    count = 0
    for row in reader:
        # if the data set row is missing a latitude or longitude
        if row[24] == "" or row[23] == "":
            continue
        longitude = float(row[24])
        latitude = float(row[23])
        if count < 10 and haversine(lng, lat, longitude, latitude) <= radius:
            incident_id = int(row[7])
            incident_date = row[1]
            incident_category = row[14]
            incident_description = row[16]
            incident_longitude = float("%.4f" % longitude)
            incident_latitude = float("%.4f" % latitude)
            relevant_incidents[incident_id]["incident_date"] = incident_date
            relevant_incidents[incident_id]["category"] = incident_category
            relevant_incidents[incident_id]["description"] = incident_description
            relevant_incidents[incident_id]["longitude"] = incident_longitude
            relevant_incidents[incident_id]["latitude"] = incident_latitude

    return relevant_incidents


"""
Creates a json file containing the relevant incident information
based on the lng, lat, and radius given
"""
def create_relevant_indicent_json(lng, lat, radius):
    relevant_incident_dict = find_relevant_incidents(lng, lat, 1)
    with open('relevant_incidents.json', 'w') as file:
        json.dump(relevant_incident_dict, file)
