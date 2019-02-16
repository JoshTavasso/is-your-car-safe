import csv
import json
import math
from collections import defaultdict

query = 'json object'

radius = '1 mile'

result = 'json file of longs and lats and content description'


#query_to_dict = json.load(query)


"""
    Calculates the great circle distance in miles between two locations given their respective 
    latitudes and longitudes in degrees.

    Formula from: https://en.wikipedia.org/wiki/Haversine_formula
"""
def haversine(long1, lat1, long2, lat2):
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
    
    great_circle_distance = earth_radius * 2 * math.asin(math.sqrt(math.sin(lat_difference/2)**2 + math.cos(lat1_radians) * math.cos(lat2_radians) * math.sin(long_difference/2)**2))

    return great_circle_distance

"""
    Gets all relevant incidents within a specified radius given a latitude and longitude in degrees.
    A dictionary of dictionaries is returned where the outer dictionary key is the incident id and
    the inner dictionary contains information such as incident category, date, description,
    latitude and longitude.
"""
def find_relevant_incidents(lng, lat, radius):
    """lat_per_mile = radius/69
    long_per_mile = radius/(69.172*math.cos(lat*math.pi/180))

    min_lat = lat - lat_per_mile
    max_lat = lat + lat_per_mile
    min_long = long - long_per_mile
    max_long = long + long_per_mile"""
    vehicle_info = open('vehicles.csv', mode='r')

    # skip header row of the csv file
    has_header = csv.Sniffer().has_header(vehicle_info.read(1024))
    vehicle_info.seek(0)
    reader = csv.reader(vehicle_info)
    if has_header:
        next(reader)

    relevant_incidents = defaultdict(dict)

    for row in reader:
        # if the data set row is missing a latitude or longitude
        if row[24] == "" or row[23] == "":
            continue
        longitude = float(row[24])
        latitude = float(row[23])
        if haversine(lng, lat, longitude, latitude) <= 1:
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

def create_relevant_indicent_json():
    relevant_incident_dict = find_relevant_incidents(-122.43776923177623, 37.75554069028438, 1)
    with open('relevant_incidents.json', 'w') as file:
        json.dump(relevant_incident_dict, file)

# used for testing functions
if __name__ == "__main__":
    create_relevant_indicent_json()