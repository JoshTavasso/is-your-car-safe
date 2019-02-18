"""
BuildDataSet.py
Builds the vehicle incident dataset needed for this application

Follow the instructions below on how to build this data set:

Export csv file of all police incidents from https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783
    
Put csv file into the main project directory and rename to "calls.csv".
    
Run python modules/BuildDataSet.py

Vehicle related incident data set should now be stored in "vehicles.csv", located in the main project directory
"""

import csv

with open('calls.csv', mode='r') as all_reports_file:
	reader = csv.reader(all_reports_file)
	with open('vehicles.csv', mode='w') as vehicle_report_outfile:
		writer = csv.writer(vehicle_report_outfile)
		writer.writerow(["Incident Datetime", "Incident Date", "Incident Time", "Incident Year", 
		"Incident Day of Week", "Report Datetime", "Row ID", "Incident ID", "Incident Number", 
		"CAD Number", "Report Type Code", "Report Type Description", "Filed Online", 
		"Incident Code", "Incident Category", "Incident Subcategory", "Incident Description", 
		"Resolution", "Intersection", "CNN", "Police District", "Analysis Neighborhood", 
		"Supervisor District", "Latitude", "Longitude", "point"])
		for row in reader:
			if "vehicle" in row[14].lower():
				writer.writerow(row)



