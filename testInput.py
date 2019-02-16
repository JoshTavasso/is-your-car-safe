import csv
import json

query = 'json object'

radius = '1 mile'

result = 'json file of longs and lats and content description'

vehicle_info = open('vehicles.csv', mode='r')
reader = csv.reader(vehicle_info)
#query_to_dict = json.loads(query)


def find_relevant_incidents(lng, lat, radius):
    pass

